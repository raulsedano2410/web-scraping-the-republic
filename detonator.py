import scrapy
from scrapy import signals


class MySpider(scrapy.Spider):
    name = "myspider"

    def __init__(
        self, keyword=None, from_date=None, to_date=None, modality=None, *args, **kwargs
    ):
        super(MySpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.from_date = from_date
        self.to_date = to_date
        self.modality = modality

    def start_requests(self):
        # Llama a la función para generar las URLs
        urls = self.generar_url()

        # Inicia las solicitudes para cada URL generada
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Extraer el texto de los elementos <a> con atributo title
        for anchor in response.xpath("//article/h1/a[@title]"):
            title_text = anchor.css("::text").get()
            yield {"title_text": title_text}

    def generar_url(self):
        # Reemplazar espacios en la palabra clave con '+'
        keyword = self.keyword.replace(" ", "+")

        # Base URL con el marcador de posición para el número de página
        url_base = "https://ricerca.repubblica.it/ricerca/repubblica?query={}&fromdate={}&todate={}&sortby=adate&author=&mode={}&page={}"

        urls = []

        # Generar URLs para las 50 páginas
        for page in range(1, 5):
            url = url_base.format(
                keyword, self.from_date, self.to_date, self.modality, page
            )
            print(url)
            # Puedes devolver las URLs en una lista en lugar de imprimirlas si lo prefieres
            urls.append(url)
        return urls
