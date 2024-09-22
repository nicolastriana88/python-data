import seaborn as sbn
import pandas as pa

data= sbn.load_dataset("titanic")

print (data.head())
print (data.info())
print (data.describe(include='all'))


# Mostrar las primera filas de dataset head()
print (data.head())


# Resumen del dataset info()
print (data.info())


# Estadística desriptivas
print(data.describe(include='all'))


# Identificación de valores faltantes
missing_data=data.isnull().sum()
print(missing_data)

# Este paso es opcional
# Eliminar columnas con más del 20% (178,2) de datos faltantes  en un total de 891.

#threshold = len(data)*0.2 # Esta configuración porcentual también es opcional

#data_cleaned = data.dropna(thresh=threshold, axis=1)

# Borrar columnas eje 1
# Borrar filas eje 0

# Eliminar filas con valores faltantes
data_cleaned_2=data.dropna()

# Elimina una columna completa
data.drop(columns=['age'])

# Rellenar valores faltantes en la columna 'age' con la mediana (1,2,[3],4,5)
data['age'].fillna(data['age'].median(), inplace=True)