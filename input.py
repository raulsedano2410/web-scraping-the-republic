def generar_url(keyword, from_date, to_date, modality):
    # Reemplazar espacios en la palabra clave con '+'
    keyword = keyword.replace(" ", "+")

    # Base URL con el marcador de posición para el número de página
    url_base = "https://ricerca.repubblica.it/ricerca/repubblica?query={}&fromdate={}&todate={}&sortby=adate&author=&mode={}&page={}"

    urls = []

    # Generar URLs para las 50 páginas
    for page in range(1, 51):
        url = url_base.format(keyword, from_date, to_date, modality, page)
        print(url)
        # Puedes devolver las URLs en una lista en lugar de imprimirlas si lo prefieres
        urls.append(url)
    return urls


# Ejemplo de llamada a la función
generar_url("mafia nigeriana", "1984-01-01", "1986-01-01", "any")
