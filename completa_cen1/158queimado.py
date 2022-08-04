import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../completa/p158.csv')

try:
    df2 = pd.read_csv('seriesvol.csv')
except:
    df2 = pd.DataFrame()
    df2.to_csv('seriesvol.csv', index=False)

try:
    df3 = pd.read_csv('vazoesreg.csv')
except:
    df3 = pd.DataFrame(index=range(1))
    df3.to_csv('vazoesreg.csv')

mes = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
t = []
for i in range(1080):
    if i <= 11:
        t.append(mes[i]+'/1931')
    else:
        iano = int(i/12) + 1931
        imes = i % 12
        t.append(mes[imes]+'/'+str(iano))

pcv = [8.017885e02,1.142334e-01,-1.977012e-04,1.44183e-07,-2.488779e-17]
pac = [-7.222541e06,2.654824e04,-3.252922e01,1.328637e-02,0.0]
vmax = 557.00
vmin = 95.25
qreg = round((vmax/200))
qsaida = qreg
valid = 0
menor = vmax
pos = 1
it = 0

print('Vazão inicial: {} m³/s.'.format(qreg))
while valid == 0:

    listavol = []
    vol = vmax

    it += 1
    if qreg < 50:
        if pos < 0.05:
            if pos < 0.02:
                qreg += 0.01
            else:
                qreg += 0.1
        else:
            qreg += 0.5
    else:
        if pos < 0.1:
            if pos < 0.05:
                if pos < 0.02:
                    if pos < 0.002:
                        qreg += 0.01
                    else:
                        qreg += 0.1
                else:
                    qreg += 0.5
            else:
                qreg += 1
        else:
            qreg += 5
    #print('\nPara vazão de saída = {} m³/s:'.format(qreg))

    for index, row in df.iterrows():
        cota = pcv[0] + (pcv[1] * vol) + (pcv[2] * (vol**2)) + (pcv[3] * (vol**3)) + (pcv[4] * (vol**4))
        area = pac[0] + (pac[1] * cota) + (pac[2] * (cota**2)) + (pac[3] * (cota**3)) + (pac[4] * (cota**4))
        evap = (row['evap'] * area)/1000
        vol = vol - evap + ((row['qnat'] - qreg) * row['conversor'])
        if vol > vmax:
            vol = vmax
            volvert = vol - vmax
        if vol < vmin:
            valid += 1
        if vol < menor:
            menor = vol
        listavol.append(vol)
        #print('Iteração {}: Volume = {}; Validador = {}.'.format(it, vol, valid))

    pos = ((menor - vmin)/(vmax - vmin))
    print('\nIteração {}:'.format(it))
    print('Para vazão de saída = {:.2f} m³/s, o menor volume alcançado é: {:.2f} m³/s, que representa {:.2f}% do intervalo de volume útil de operação.'.format(qreg, menor, pos*100))

qreg = qreg - 0.01
print('\n\nA vazão máxima regularizável é de {:.2f} m³/s.\n'.format(qreg))

serie = pd.Series(listavol)
df2 = df2.assign(queimado=serie.values)
df2.to_csv('seriesvol.csv', index=False)

df3['queimado'] = qreg
df3.to_csv('vazoesreg.csv', index=False)

fig, graf = plt.subplots()
graf.plot(t,listavol)
graf.xaxis.set_major_locator(plt.MaxNLocator(9))
plt.show()