import pandas as pd

# Cargar los datos procesados
df = pd.read_csv("earth_like_exoplanets.csv")

# Agrupar por año y contar descubrimientos
yearly_discoveries = df.groupby('disc_year').size().reset_index(name='count')

# Filtrar años significativos (por ejemplo, años con más de 5 descubrimientos)
significant_years = yearly_discoveries[yearly_discoveries['count'] > 5]['disc_year'].tolist()

# Filtrar los datos para incluir solo años significativos
filtered_data = df[df['disc_year'].isin(significant_years)]

# Guardar los datos filtrados en JSON
filtered_data.to_json("timeline_data.json", orient="records")