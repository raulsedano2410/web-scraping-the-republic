import csv


def remove_empty_rows(input_file, output_file):
    with open(input_file, "r", newline="") as f_input:
        with open(output_file, "w", newline="") as f_output:
            csv_reader = csv.reader(f_input)
            csv_writer = csv.writer(f_output)
            for row in csv_reader:
                if any(row):
                    csv_writer.writerow(row)


# Define el nombre de tu archivo de entrada y salida
input_file = "visited_urls.csv"
output_file = "visited_urls_1_5.csv"

# Llama a la función para eliminar las filas vacías
remove_empty_rows(input_file, output_file)
