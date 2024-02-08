import csv


def compare_csv_urls(file1, file2):

    # Leer líneas de cada archivo CSV
    with open(file1) as f1:
        reader1 = csv.reader(f1)
        urls1 = [row[0] for row in reader1]

    with open(file2) as f2:
        reader2 = csv.reader(f2)
        urls2 = [row[0] for row in reader2]

    # Convertir las listas a conjuntos para poder
    # usar operaciones de conjuntos más eficientemente
    unique_urls1 = set(urls1)
    unique_urls2 = set(urls2)

    # Verificar si los conjuntos son iguales,
    # esto nos dice si los CSVs tienen las mismas URLs
    print(unique_urls1 == unique_urls2)

    # Encontrar urls en un archivo pero no en el otro
    only_in_file1 = unique_urls1 - unique_urls2
    only_in_file2 = unique_urls2 - unique_urls1

    print(f"Sólo en File 1: {len(only_in_file1)}")
    print(f"Sólo en File 2: {len(only_in_file2)}")


# Ejemplo de uso:
compare_csv_urls("../visited_urls_3_5.csv", "../visited_urls_2_5.csv")
