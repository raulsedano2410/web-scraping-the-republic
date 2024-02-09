import csv  # CSV file reading and writing
import os  # For file system operations like checking paths
import scrapy  # Library for web scraping

from bs4 import BeautifulSoup  # HTML parsing

import time


# File to store already visited urls
visited_urls_file = "visited_urls_3_5.csv"

# CSV file containing the start URLs to crawl
start_urls_csv = "mafia_nigeriana_2009-02-24_2024-01-01.csv"


# Spider class to handle crawling news articles
class MySpider(scrapy.Spider):
    name = "myspider"

    # Method that initiates requests
    def start_requests(self):

        # Check if visited URLS file exists to see if this
        # is a first run or a continuation after failure
        if os.path.exists(visited_urls_file):

            # Open the file and create a set of already visited URLs
            with open(visited_urls_file) as f:
                reader = csv.reader(f)
                visited_urls = {row[0] for row in reader if row}
        else:
            # If file does not exist, this is a first run
            visited_urls = set()

        # Open starting URL csv and iterate through
        with open(start_urls_csv, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                url = row["URL"]

                # Check URL against already visited
                if url not in visited_urls:
                    visited_urls.add(url)

                    # Yield the scraping request
                    yield scrapy.Request(url=url, callback=self.parse)

    # Method that handles parsing the response
    def parse(self, response):

        # Select all article elements from page
        articles = response.css("article")

        # List to store extracted article data
        article_data = []

        for article in articles:

            # Get the inner HTML of title anchor tag
            anchor_html = article.css("h1 a").extract_first()

            # Use BeautifulSoup to parse HTML
            soup = BeautifulSoup(anchor_html, "html.parser")

            # Extract clean text for title
            title = soup.get_text(separator=" ", strip=True)

            # Extract article link
            link = article.css("h1 a::attr(href)").get()

            # Extract publish date
            date = article.css("aside a time::text").get()

            # Append article data to list
            article_data.append(
                {
                    "title": title,
                    "link": link,
                    "date": date,
                    "page_url": response.url,
                    # Puedes agregar más campos según tus necesidades
                }
            )
        # Write extracted article data to CSV file
        with open("output.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["title", "link", "date", "page_url"]
            )

            # Write header if file is empty
            if os.stat("output.csv").st_size == 0:
                writer.writeheader()

            # Write row for each article data
            for data in article_data:
                writer.writerow(data)

        # Append url to visited file
        with open(visited_urls_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([response.url])

    # Method called when spider is closed
    def closed(self, reason):

        # Log reason for spider closure
        self.log("Spider cerrado: " + reason)

    # Configuración de los middlewares
    # Método para manejar errores de respuesta HTTP
    def process_exception(self, request, exception, spider):
        if (
            isinstance(exception, scrapy.http.HttpError)
            and exception.response.status == 403
        ):
            # Loguea el error 403
            spider.log(f"Recibido error 403 en {request.url}")

            # Espera 6 minutos antes de volver a intentar la solicitud
            spider.log("Esperando 6 minutos antes de volver a intentar la solicitud...")
            time.sleep(360)
            return scrapy.Request(
                request.url, callback=request.callback, dont_filter=True
            )
