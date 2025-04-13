import csv
import json

# Nombre del archivo CSV inicial
csv_file = 'earth_like_exoplanets.csv'  # Asegúrate de que este archivo esté en el mismo directorio
output_json = 'timeline.json'

# Leer el archivo CSV y procesar los datos
planets_by_year = {}
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extraer la información relevante
        year = int(row['disc_year'])
        planet_name = row['pl_name']
        esi = float(row['ESI']) if row['ESI'] else 0  # Convertir ESI a float, usar 0 si está vacío
        radius = float(row['pl_rade']) if row['pl_rade'] else None  # Convertir radio a float, usar None si está vacío

        # Si el año no está en el diccionario, inicializar la lista
        if year not in planets_by_year:
            planets_by_year[year] = []

        # Agregar el planeta a la lista del año correspondiente
        planets_by_year[year].append({
            "disc_year": year,
            "pl_name": planet_name,
            "ESI": esi,
            "pl_rade": radius
        })

# Convertir el diccionario a una lista ordenada por año
timeline = []
for year in sorted(planets_by_year.keys()):
    timeline.extend(planets_by_year[year])

# Guardar los datos en un archivo JSON
with open(output_json, 'w', encoding='utf-8') as file:
    json.dump(timeline, file, indent=4)

print(f"Archivo {output_json} generado correctamente.")