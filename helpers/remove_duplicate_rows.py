import csv

def remove_duplicate_rows(input_file, output_file, duplicates_file):

  duplicate_rows = set()

  with open(input_file, encoding="utf-8") as f_input:
    reader = csv.reader(f_input)

    rows_set = set()
    for row in reader:
        row = tuple(row) # Convertir
        if row in rows_set:
            duplicate_rows.add(row)
        else:
           rows_set.add(row)

  with open(output_file, 'w', newline='', encoding="utf-8") as f_output:
      writer = csv.writer(f_output)
      for row in rows_set:
          writer.writerow(row)

  # Guardar filas duplicadas a un nuevo archivo
  with open(duplicates_file, 'w', newline='', encoding="utf-8") as f_duplicates:
      writer = csv.writer(f_duplicates)
      for row in duplicate_rows:
          writer.writerow(row)

# Ejemplo de uso:
input_file = "data.csv"
output_file = "sin_duplicados.csv"
duplicates_file = "duplicados.csv"

remove_duplicate_rows("../output_v1_outdate.csv", "output_v1_clean.csv", "output_repeat_list.csv")
