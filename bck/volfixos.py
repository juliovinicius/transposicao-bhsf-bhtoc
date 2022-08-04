import pandas as pd

df = pd.read_csv('seriesvol.csv')

vol = {}

vol['pamx'] = [1226.00 for i in range(1080)]
vol['xingo'] = [3800.00 for i in range(1080)]
vol['canabrava'] = [2300.00 for i in range(1080)]
vol['saosalvador'] = [952.00 for i in range(1080)]
vol['estreito'] = [5400.00 for i in range(1080)]
vol['lajeado'] = [4940.00 for i in range(1080)]

u1 = pd.Series(vol['pamx'])
u2 = pd.Series(vol['xingo'])
u3 = pd.Series(vol['canabrava'])
u4 = pd.Series(vol['saosalvador'])
u5 = pd.Series(vol['estreito'])
u6 = pd.Series(vol['lajeado'])

df = df.assign(pamx=u1.values,xingo=u2.values,canabrava=u3.values,saosalvador=u4.values,estreito=u5.values,lajeado=u6.values)
print(df)
df.to_csv('seriesvol.csv')