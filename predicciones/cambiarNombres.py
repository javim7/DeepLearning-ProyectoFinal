import csv
import os

# Directorio donde se encuentran los archivos CSV
directorio = 'predicciones/jornadas'  # Reemplaza con la ruta adecuada
directorio_modificado = 'predicciones/jornadasMod'

# Asegúrate de que el directorio modificado exista, si no, créalo
if not os.path.exists(directorio_modificado):
    os.makedirs(directorio_modificado)

# Función para realizar la modificación del nombre del equipo
def modificar_nombre(nombre_equipo):
    if nombre_equipo == 'Almería':
        return 'Almeria'
    elif nombre_equipo == 'Athletic':
        return 'Ath Bilbao'
    elif nombre_equipo == 'Atlético':
        return 'Ath Madrid'
    elif nombre_equipo == 'Cádiz':
        return 'Cadiz'
    elif nombre_equipo == 'Deportivo Alavés':
        return 'Alaves'
    elif nombre_equipo == 'Rayo Vallecano':
        return 'Vallecano'
    elif nombre_equipo == 'Real Betis':
        return 'Betis'
    elif nombre_equipo == 'Real Sociedad':
        return 'Sociedad'
    else:
        return nombre_equipo

# Iterar sobre todos los archivos CSV en el directorio
for filename in os.listdir(directorio):
    if filename.endswith(".csv"):
        input_csv_file = os.path.join(directorio, filename)
        output_csv_file = os.path.join(directorio_modificado, filename)

        with open(input_csv_file, 'r', encoding='utf-8', newline='') as input_file, open(output_csv_file, 'w', encoding='utf-8', newline='') as output_file:
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)

            # Escribir la primera fila (encabezados)
            csv_writer.writerow(next(csv_reader))

            # Iterar a través de las filas restantes y modificar el nombre del equipo
            for row in csv_reader:
                row[1] = modificar_nombre(row[1])
                csv_writer.writerow(row)

        print(f"Proceso completado para {filename}. Se ha creado el archivo modificado_{filename}.")
