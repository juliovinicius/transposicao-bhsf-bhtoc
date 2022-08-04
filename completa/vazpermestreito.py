import pandas as pd


vaz = pd.read_csv('vaznat.csv')
vazest = vaz['estreito']

vazoesantiga = []
vazoesnova = []
t = []
meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
seriemes = {'Jan': [],'Fev': [],'Mar': [],'Abr': [],'Mai': [],'Jun': [],'Jul': [],'Ago': [],'Set': [],'Out': [],'Nov': [],'Dez': []}
seriemesdesc = {'Jan': [],'Fev': [],'Mar': [],'Abr': [],'Mai': [],'Jun': [],'Jul': [],'Ago': [],'Set': [],'Out': [],'Nov': [],'Dez': []}
permmes = {'Jan': [],'Fev': [],'Mar': [],'Abr': [],'Mai': [],'Jun': [],'Jul': [],'Ago': [],'Set': [],'Out': [],'Nov': [],'Dez': []}
q95 = {'Jan': [],'Fev': [],'Mar': [],'Abr': [],'Mai': [],'Jun': [],'Jul': [],'Ago': [],'Set': [],'Out': [],'Nov': [],'Dez': []}

#lista com as datas
for i in range(1080):
	if i <= 11:
		t.append(meses[i]+'/1931')
	else:
		iano = int(i/12) + 1931
		imes = i % 12
		t.append(meses[imes]+'/'+str(iano))

#separando as vazões entre pré-1993 e pós-1993
i = 1
for val in vazest:
	if i < 745:
		vazoesantiga.append(val)
	if i >= 745:
		vazoesnova.append(val)
	i += 1

vazoesnovadesc = []
for val in vazoesnova:
	vazoesnovadesc.append(val)
vazoesantigadesc = []
for val in vazoesantiga:
	vazoesantigadesc.append(val)

#colocando as duas séries de vazões em ordem decrescente
vazoesnovadesc.sort(reverse=True)
vazoesantigadesc.sort(reverse=True)

#calculando a permanência para os 2 períodos
permnova = []
permantiga = []
i = 1
for val in vazoesnovadesc:
	permnova.append(i/len(vazoesnovadesc))
	i += 1
i = 1
for val in vazoesantigadesc:
	permantiga.append(i/len(vazoesantigadesc))
	i += 1

# for i in range(len(vazoesnovadesc)):
# 	print('Vazão: {} / Permanência: {:.2f}% / Índice: {}'.format(vazoesnovadesc[i],permnova[i]*100,t[i+744]))
#print(sum(vazoesantiga)/len(vazoesantiga))

vazestdesc = []
vazestdesc = vazest.sort_values(ascending=False)

for i in range(len(vazest)):
	print('{} / {}'.format(i,t[i]))

#calculando a permanência para a série inteira
perm = []
vazoes = []
i = 1
for val in vazestdesc:
	vazoes.append(val)
	perm.append(i/len(vazestdesc))
	i += 1

# for i in range(len(vazest)):
# 	print('Vazão: {} / Permanência: {:.2f}%'.format(vazoes[i],perm[i]*100))

#preenchendo o dicionário de séries para cada mês
i = 0
for val in vazoesnova:
	if i == 12:
		i = 0
	seriemes[meses[i]].append(val)
	i += 1

#print(vazoesnova)
#print('\n\n\n')
#print(seriemes)

for mes in seriemes:
	for val in seriemes[mes]:
		seriemesdesc[mes].append(val)
	seriemesdesc[mes].sort(reverse=True)

#print('\n\n')
#print(seriemesdesc)

#calculando a permanência para as séries de cada mês
for mes in seriemesdesc:
	i = 1
	for val in seriemesdesc[mes]:
		permmes[mes].append(i/len(seriemesdesc[mes]))
		i += 1
#print(permmes)

#calculando o q95 para cada mês
for mes in permmes:
	for i in range(len(permmes[mes])):
		if permmes[mes][i] >= 0.95:
			q95[mes] = seriemesdesc[mes][i-1] * permmes[mes][i-1] / 0.95
			break
	print('Mês: {} / Q95: {:.2f} m³/s'.format(mes,q95[mes]))