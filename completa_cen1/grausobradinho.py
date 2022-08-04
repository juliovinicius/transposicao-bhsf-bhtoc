import pandas as pd
import matplotlib.pyplot as plt

mes = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
t = []
listagrau = []
mediaanoqnat = 2523.204474885845
for i in range(1080):
    if i <= 11:
        t.append(mes[i]+'/1931')
    else:
        iano = int(i/12) + 1931
        imes = i % 12
        t.append(mes[imes]+'/'+str(iano))

df = pd.read_csv('../completa/p169.csv')

try:
    df2 = pd.read_csv('seriesgrau.csv')
except:
    df2 = pd.DataFrame()
    df2.to_csv('seriesgrau.csv', index=False)

pcv = [3.74179e02,1.39669e-03,-5.35159e-08,1.155989e-12,-9.545989e-18]
pac = [-5.03710e05,4.913789e03,-8.966889,-1.89169e-02,4.65379e-05]
percent = [0.1366,0.1460,0.1812,0.1578,0.0909,0.0471,0.0327,0.0249,0.0212,0.0263,0.0459,0.0893]
vmax = 34116.00
vmin = 5447.00
qref = 500.00

while qref <= 2000:
    print('Para Qref de {} m³/s.\n'.format(qref))

    valid = 0
    transp = []
    it = 0
    pos = 1
    menor = vmax
    qreg = round((vmax/200))

    for pmes in percent:
        transp.append(qref*pmes/(1/12))
    print('Valores de transposição: {}.'.format(transp))

    while valid == 0:

        listavol = []
        vol = vmax
        i = 0
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
            if i == 12:
                i = 0
            cota = pcv[0] + (pcv[1] * vol) + (pcv[2] * (vol**2)) + (pcv[3] * (vol**3)) + (pcv[4] * (vol**4))
            area = pac[0] + (pac[1] * cota) + (pac[2] * (cota**2)) + (pac[3] * (cota**3)) + (pac[4] * (cota**4))
            evap = (row['evap'] * area)/1000
            vol = vol - evap + ((row['qnat'] + transp[i] - qreg) * row['conversor'])
            if vol > vmax:
                vol = vmax
                volvert = vol - vmax
            if vol < vmin:
                valid += 1
            if vol < menor:
                menor = vol
            listavol.append(vol)
            #print('Iteração {}: Volume = {}; Validador = {}.'.format(it, vol, valid))
            i += 1

        pos = ((menor - vmin)/(vmax - vmin))
        print('\nIteração {}:'.format(it))
        print('Vazão de saída = {:.2f} m³/s / Menor volume alcançado: {:.2f} m³/s, que representa {:.2f}% do intervalo de volume útil de operação.'.format(qreg, menor, pos*100))

    qreg = qreg - 0.01
    print('\n\nA vazão máxima regularizável para a vazão de referência de {} é de {:.2f} m³/s.\n'.format(qref, qreg))
    listagrau.append(100*qreg/mediaanoqnat)
    qref += 20.00

serie = pd.Series(listagrau)
df2 = df2.assign(sobradinho=serie.values)
df2.to_csv('seriesgrau.csv', index=False)

