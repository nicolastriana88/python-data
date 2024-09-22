import pandas as pd
import seaborn as sb

notas = r'C:\Users\NTZ\Documents\notas.csv'


df = pd.read_csv(notas)


df["Nota final"] =df ["Nota 1"] * 0.3 + df["Nota 2"] * 0.3 + df["Nota 3"] * 0.4 % 3

print(df.head())