"""
# Leer el archivo y mostrar las primeras líneas para entender su estructura
file_path = '/mnt/data/pubmed-HealthWork-set.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

# Mostrar las primeras líneas para analizar
lines[:20]

"""

"""import pandas as pd

# Inicializar una lista para almacenar cada registro
records = []
current_record = {}

# Función para agregar un registro a la lista de registros
def add_record(record):
    if record:
        records.append(record)

# Procesar cada línea
for line in lines:
    if line.startswith('PMID-'):
        add_record(current_record)
        current_record = {}
    
    # Separar el campo de su valor
    if '-' in line:
        key, value = line.split('-', 1)
        key = key.strip()
        value = value.strip()
        
        if key in current_record:
            current_record[key] += ' ' + value
        else:
            current_record[key] = value
    else:
        # Para líneas que no tienen '-', asumir que es continuación del valor previo
        if key in current_record:
            current_record[key] += ' ' + line.strip()

# Agregar el último registro
add_record(current_record)

# Convertir la lista de registros en un DataFrame de pandas
df = pd.DataFrame(records)

# Guardar el DataFrame en un archivo CSV
output_path = '/mnt/data/pubmed-HealthWork-set.csv'
df.to_csv(output_path, index=False)
output_path
"""


import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('pubmed-HealthWork-set.csv')

# Concatenar todas las columnas de abstract en una sola columna
abstract_columns = [col for col in df.columns if col.startswith('AB')]

# Combinar los abstracts dispersos
df['Abstract'] = df[abstract_columns].apply(lambda row: ' '.join(row.dropna().astype(str)), axis=1)

# Eliminar las columnas originales de abstract
df.drop(columns=abstract_columns, inplace=True)

# Guardar el DataFrame corregido en un nuevo archivo CSV
output_corrected_path = 'pubmed-HealthWork-set-corrected.csv'
df.to_csv(output_corrected_path, index=False)
output_corrected_path