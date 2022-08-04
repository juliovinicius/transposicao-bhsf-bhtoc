
import pandas as pd

df = pd.read_csv('p275.csv')

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

pcv = [3.178443e01,2.392409e-03,-6.748674e-08,1.047067e-12,-6.345606e-18]
pac = [2.550023e05,-1.625751e04,3.855196e02,-4.029465,1.576732e-02]
vmax = 50275.00
vmin = 11293.00
qreg = round((vmax/1000))
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
df2 = df2.assign(tucurui=serie.values)
#print(df2)
df2.to_csv('seriesvol.csv', index=False)

df3['tucurui'] = qreg
df3.to_csv('vazoesreg.csv', index=False)