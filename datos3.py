import pandas as pd
import seaborn as sb

notas = r'C:\Users\NTZ\Documents\notas.csv'


df = pd.read_csv(notas)

# Lista los primeros 5 registros
df.head()

# Lista los primeros 2 registros
df.head(2)

# Lista los últimos 5 registros
df.tail()

# Lista los últimos 2 registros
df.tail(2)

# Muestra un registro al azar
df.sample()

# Muestra 2 registros al azar
df.sample(2)

# Muestra estadísticas básicas del DF
df.describe()


# Muestra datos de una columna
df["Nota 1"]

# Muestra datos de varias columnas
df[["Nombre","Nota 1","Nota 3"]]

# Crea nueva columna
df["Nombre Completo"] = df["Nombre"] + " " + df["Apellido"]
df

# Crea nueva columna
df["Nota 5"] = df["Nota 1"] / (df["Nota 3"] * df["Nota 2"])
df

# Consultar con una condición
df["Nota"] > 20

# Consultar con más de una condición
(df["Nota 1"] > 3.0) & (df["Nota 2"] > 3.0)

# Filtrar registros con condiciones
df[(df["Nombre"] > 20) & (df["Nota 2"] > 1.60)]

# Agrupar por determinada característica
# Sería como Select Altura, count(*) from df group by Altura;
df.groupby("Nombre").size()


df["Nota final"] =df ["Nota 1"] * 0.3 + ["Nota 2"] * 0.3 + ["Nota 1"] * 0.4 % 3
