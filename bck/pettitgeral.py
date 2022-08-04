import pandas as pd
import pyhomogeneity as hg

uhes = ['retirobaixo','tresmarias','queimado','sobradinho','itaparica','pamx','xingo','serradamesa','canabrava','peixeangelical','saosalvador','lajeado','estreito','tucurui']
bacias = ['bhsf','bhtoc']

qnat = pd.read_csv('qnatgeral.csv')
ena = pd.read_csv('seriesena.csv')

seriesano = {}
seriesena = {}

for uhe in uhes:
	#print('\n\nPara UHE {}:'.format(uhe))
	seriesano[uhe] = []
	anob = 2
	imes = 0
	aux = []
	for i, r in qnat.iterrows():
		if (imes%12) == 0 and imes > 0:
			imes = 0
			if anob == 3:
				seriesano[uhe].append(sum(aux)/366)
				#print(seriesano[uhe])
			else:
				seriesano[uhe].append(sum(aux)/365)
				#print(seriesano[uhe])
			aux = []
			anob += 1
		if anob == 4:
			anob = 0
		if imes in (0,2,4,6,7,9,11):
			aux.append(r[uhe]*31)
			#print(aux, '31')
		if imes == 1:
			if anob == 3:
				aux.append(r[uhe]*29)
				#print(aux, '29')
			else:
				aux.append(r[uhe]*28)
				#print(aux, '28')
		if imes in (3,5,8,10):
			aux.append(r[uhe]*30)
			#print(aux, '30')
		imes += 1

pettitt = {}
'''for uhe in uhes:
	pettitt[uhe] = hg.pettitt_test(seriesano[uhe])
	print('Para UHE {}: {}.'.format(uhe,pettitt[uhe]))
'''

for bacia in bacias:
	#print('\n\nPara UHE {}:'.format(uhe))
	seriesena[bacia] = []
	anob = 2
	imes = 0
	aux = []
	for i, r in ena.iterrows():
		if (imes%12) == 0 and imes > 0:
			imes = 0
			if anob == 3:
				seriesena[bacia].append(sum(aux)/366)
				#print(seriesano[uhe])
			else:
				seriesena[bacia].append(sum(aux)/365)
				#print(seriesano[uhe])
			aux = []
			anob += 1
		if anob == 4:
			anob = 0
		if imes in (0,2,4,6,7,9,11):
			aux.append(r[bacia]*31)
			#print(aux, '31')
		if imes == 1:
			if anob == 3:
				aux.append(r[bacia]*29)
				#print(aux, '29')
			else:
				aux.append(r[bacia]*28)
				#print(aux, '28')
		if imes in (3,5,8,10):
			aux.append(r[bacia]*30)
			#print(aux, '30')
		imes += 1

for bacia in bacias:
	pettitt[bacia] = hg.pettitt_test(seriesena[bacia])
	print('\nPara bacia {}: {}.'.format(bacia,pettitt[bacia]))

for uhe in uhes:
	pettitt[uhe] = hg.pettitt_test(seriesano[uhe])
	print('\nPara UHE {}: {}.'.format(uhe,pettitt[uhe]))