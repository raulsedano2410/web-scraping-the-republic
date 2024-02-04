import scrapy
import json

class MySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        # Cargar las URLs desde el archivo JSON
        with open('links.json', 'r') as file:
            urls = json.load(file)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Raspar todos los elementos <article>
        articles = response.css('article')

        # Lista para almacenar datos de cada artículo en la página
        page_data = []

        for article in articles:
            # Extraer título del artículo (h1)
            title = article.css('h1 a::text').get()

            link = article.css('h1 a::attr(href)').get()

            date = article.css('aside a time::text').get()

            # Agregar datos al array
            page_data.append({
                "title": title,
                "link": link,
                "date": date,
                # Puedes agregar más campos según tus necesidades
            })

        # Guardar los datos en un archivo JSON
        output_file = 'output.json'
        with open(output_file, 'a') as file:
            json.dump(page_data, file, indent=2)

        self.log(f'Data extracted from {response.url} and saved to {output_file}')
