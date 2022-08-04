import pandas as pd

df = pd.read_csv('p191.csv')
serie = pd.Series(df['conversor'])
df2 = pd.read_csv('p273.csv')
df2 = df2.assign(conversor=serie.values)
df2.to_csv('p273.csv')