import pandas as pd
import seaborn as sb

personas = r'C:\Users\NTZ\Documents\personas.csv'


df = pd.read_csv(personas)

print(df.head())