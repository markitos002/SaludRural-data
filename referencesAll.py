import pandas as pd
import re


# Cargar las referencias desde un archivo CSV
df = pd.read_csv('pubmed-HealthWork-set-corrected.csv')

# Lista de palabras clave
palabras_clave = ['Physician']

# Crear una expresión regular que busque cualquier palabra clave
patron = re.compile('|'.join(palabras_clave), re.IGNORECASE)

# Filtrar las referencias cuyos resúmenes contienen alguna de las palabras clave
df_filtrado = df[df['Abstract'].apply(lambda x: bool(patron.search(str(x))))]

# Guardar las referencias filtradas en un nuevo archivo CSV
df_filtrado.to_csv('referencias_phys.csv', index=False)

print("Proceso completado. Se han guardado las referencias filtradas en 'referencias_filtradas.csv'.")


df1 = pd.read_csv('referencias_nurse.csv')
df2 = pd.read_csv('referencias_phys.csv')

df3 = pd.concat([df1, df2], ignore_index=True)

df3.to_csv('referencias_join.csv', index=False)

print("Proceso completado. Se han guardado las referencias filtradas en 'referencias_join.csv'.")