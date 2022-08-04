import numpy as np
import pyhomogeneity as hg
import csv

def pettitt_test1(X):
    """
    Pettitt test calculated following Pettitt (1979): https://www.jstor.org/stable/2346729?seq=4#metadata_info_tab_contents
    """

    T = len(X)
    U = []
    for t in range(T): # t is used to split X into two subseries
        X_stack = np.zeros((t, len(X[t:]) + 1), dtype=int)
        X_stack[:,0] = X[:t] # first column is each element of the first subseries
        X_stack[:,1:] = X[t:] # all rows after the first element are the second subseries
        U.append(np.sign(X_stack[:,0] - X_stack[:,1:].transpose()).sum()) # sign test between each element of the first subseries and all elements of the second subseries, summed.

    tau = np.argmax(np.abs(U)) # location of change (first data point of second sub-series)
    K = np.max(np.abs(U))
    p = 2 * np.exp(-6 * K**2 / (T**3 + T**2))
        
    return (tau, p)

dados = {'anual': [],
'janeiro': [],
'fevereiro': [],
'março': [],
'abril': [],
'maio': [],
'junho': [],
'julho': [],
'agosto': [],
'setembro': [],
'outubro': [],
'novembro': [],
'dezembro': []}

#ler o csv e inputar os dados no dicionário
with open('estreito.csv', 'r') as f:
    data = f.read()
    data = data.split('\n')
    for i in data:
        i = i.split(';')
        aux = []
        for j in i:
            aux.append(float(j))
        dados['anual'].append(aux[0])
        dados['janeiro'].append(aux[1])
        dados['fevereiro'].append(aux[2])
        dados['março'].append(aux[3])
        dados['abril'].append(aux[4])
        dados['maio'].append(aux[5])
        dados['junho'].append(aux[6])
        dados['julho'].append(aux[7])
        dados['agosto'].append(aux[8])
        dados['setembro'].append(aux[9])
        dados['outubro'].append(aux[10])
        dados['novembro'].append(aux[11])
        dados['dezembro'].append(aux[12])


for i in dados:
    resultfunc = pettitt_test1(dados[i])
    resulthg = hg.pettitt_test(dados[i])

    print('O resultado para a série {} pela função é de:\n{}\nJá pelo pacote pyHomogeneity é:\n{}.'.format(i, resultfunc, resulthg))
    print('----------------')
#resultadofunc = pettitt_test1(dados)
#resultadohom = hg.pettitt_test(dados)
