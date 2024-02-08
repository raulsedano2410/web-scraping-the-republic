import csv


def verificar_fechas(csv_file):
    fechas_faltantes = []  # Lista para almacenar los índices de las filas sin fecha

    # Leer el archivo CSV y encontrar las filas sin fecha
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            if "date" not in row or not row["date"]:
                fechas_faltantes.append(idx)

    # Imprimir el número de filas sin fecha
    num_fechas_faltantes = len(fechas_faltantes)
    print(f"Número de filas sin fecha: {num_fechas_faltantes}")

    # Imprimir los índices de las filas sin fecha
    print("\nÍndices de las filas sin fecha:")
    for idx in fechas_faltantes:
        print(idx)

    # Retornar la lista de índices de las filas sin fecha
    return fechas_faltantes


# Llamar a la función con tu archivo CSV
verificar_fechas("../output_10.csv")
