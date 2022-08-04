
import pandas as pd
import matplotlib.pyplot as plt

#parâmetros cota x volume
pcv = {'retirobaixo': [5.915352e02,1.642508e-01,-2.607112e-04,0.0,0.0],
'tresmarias': [5.303318e02,6.07596e-03,-4.83615e-07,2.203479e-11,-3.84658e-16],
'queimado': [8.017885e02,1.142334e-01,-1.977012e-04,1.44183e-07,-2.488779e-17],
'sobradinho': [3.74179e02,1.39669e-03,-5.35159e-08,1.155989e-12,-9.545989e-18],
'itaparica': [2.75813e02,6.764889e-03,-8.86837e-07,7.067909e-11,-2.23985e-15],
'peixeangelical': [2.392818e02,2.91567e-02,-1.80209e-05,5.657203e-09,-6.60896e-13],
'serradamesa': [3.914048e02,2.77216e-03,-4.35725e-08,2.90304e-13,0.0],
'tucurui': [3.178443e01,2.392409e-03,-6.748674e-08,1.047067e-12,-6.345606e-18]}

#volumes mínimos e máximos (hm³)
limitevol = {'retirobaixo': [200.72,241.59],
'tresmarias': [4250.00,19528.00],
'queimado': [95.25,557.00],
'sobradinho': [5447.00,34116.00],
'itaparica': [7234.00,10782.00],
'peixeangelical': [2212.70,2741.00],
'serradamesa': [11150.00,54400.00],
'tucurui': [11293.00,50275.00],
'pamx': [1226.00,1226.00],
'xingo': [3800.00,3800.00],
'canabrava': [2300.00,2300.00],
'saosalvador': [952.00,952.00],
'estreito': [5400.00,5400.00],
'lajeado': [4940.00,4940.00]}

#cotas mínimas e máximas (m)
limitecotas = {'retirobaixo': [614.00,616.00],
'tresmarias': [549.20,572.50],
'queimado': [811.00,829.00],
'sobradinho': [389.50,392.50],
'itaparica': [299.00,304.00],
'peixeangelical': [261.00,263.00],
'serradamesa': [417.30,460.00],
'tucurui': [51.60,74.00],
'pamx': [251.50,251.50],
'xingo': [138.00,138.00],
'canabrava': [333.00,333.00],
'saosalvador': [287.00,287.00],
'estreito': [156.00,156.00],
'lajeado': [212.00,212.00]}

#produtibilidade específica (MW.s/m4)
prodesp = {'retirobaixo': 0.008755,
'tresmarias': 0.008804,
'queimado': 0.008957,
'sobradinho': 0.008917,
'itaparica': 0.008710,
'pamx': 0.009035,
'xingo': 0.009014,
'serradamesa': 0.009082,
'canabrava': 0.008927,
'saosalvador': 0.009016,
'peixeangelical': 0.009060,
'lajeado': 0.008612,
'estreito': 0.009082,
'tucurui': 0.009065}

#cota de fuga média (m)
cotafuga = {'retirobaixo': 577.48,
'tresmarias': 516.24,
'queimado': 638.79,
'sobradinho': 362.34,
'itaparica': 251.31,
'pamx': 138.00,
'xingo': 17.01,
'serradamesa': 334.76,
'canabrava': 288.46,
'saosalvador': 262.57,
'peixeangelical': 235.64,
'lajeado': 176.07,
'estreito': 132.62,
'tucurui': 7.17}

#cotas de referência (m)
cotaref = {'retirobaixo': 616.00,
'tresmarias': 572.71,
'queimado': 829.00,
'sobradinho': 392.52,
'itaparica': 303.98,
'pamx': 251.50,
'xingo': 138.00,
'serradamesa': 460.00,
'canabrava': 332.53,
'saosalvador': 286.87,
'peixeangelical': 263.00,
'lajeado': 212.04,
'estreito': 155.40,
'tucurui': 74.00}

#ordem na bacia do são francisco
bhsf = ['retirobaixo','tresmarias','queimado','sobradinho','itaparica','pamx','xingo']

#ordem na bacia do tocantins
bhtoc = ['serradamesa','canabrava','saosalvador','peixeangelical','lajeado','estreito','tucurui']

#cotas geométricas
cotageo = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#cotas geométricas máximas
cotageomax = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#perdas
perda = {'retirobaixo': [],
'tresmarias': [0.7 for i in range(1080)],
'queimado': [2.91 for i in range(1080)],
'sobradinho': [0.2 for i in range(1080)],
'itaparica': [0.52 for i in range(1080)],
'pamx': [0.6 for i in range(1080)],
'xingo': [0.84 for i in range(1080)],
'serradamesa': [1.27 for i in range(1080)],
'canabrava': [0.9 for i in range(1080)],
'saosalvador': [0.64 for i in range(1080)],
'peixeangelical': [0.47 for i in range(1080)],
'lajeado': [0.22 for i in range(1080)],
'estreito': [0.39 for i in range(1080)],
'tucurui': [0.29 for i in range(1080)]}

#queda líquida equivalente (m)
heq = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#queda líquida equivalente máxima (m)
heqmax = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#produtibilidade equivalente (MW.s/m3)
prodeq = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#produtibilidade equivalente máxima (MW.s/m3)
prodeqmax = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#EAR
EAR = {'retirobaixo': [],
'tresmarias': [],
'queimado': [],
'sobradinho': [],
'itaparica': [],
'pamx': [],
'xingo': [],
'serradamesa': [],
'canabrava': [],
'saosalvador': [],
'peixeangelical': [],
'lajeado': [],
'estreito': [],
'tucurui': []}

#EARbacia
EARbacia = {'BHSF': [],
'BHTOC': []}

#EARmax
EARmax = {}

#EARbaciamax
EARbaciamax = {'BHSF': [],
'BHTOC': []}

#proporção de EAR
propEAR = {}

#somatório auxiliar para cálculo da qmlt
somaano = {}

#médias anuais de qnat
mediaanoqnat = {}

#vazão média de longo termo
qmlt = {}

#grau de regularização
grau = {}

#períodos críticos em potencial
pcs = {'BHSF': {},
'BHTOC': {}}

#conversor de meses do ano
mes = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']

nomes = {'retirobaixo': 'Retiro Baixo',
'tresmarias': 'Três Marias',
'queimado': 'Queimado',
'sobradinho': 'Sobradinho',
'itaparica': 'Itaparica',
'pamx': 'Paulo Afonso/Moxotó',
'xingo': 'Xingó',
'serradamesa': 'Serra da Mesa',
'canabrava': 'Cana Brava',
'saosalvador': 'São Salvador',
'peixeangelical': 'Peixe Angelical',
'lajeado': 'Lajeado',
'estreito': 'Estreito',
'tucurui': 'Tucuruí'}

#volume a 65%
vol_65 = {}

#cota com volume a 65%
cota_65 = {}

#perda com volume a 65%
perda_65 = {}

#cota geométrica com volume a 65%
cotageo_65 = {}

#queda equivalente com volume a 65%
heq_65 = {}

#produtibilidade equivalente a 65%
prodeq_65 = {}

#ENA
ENA = {}

#ENAbacia
ENAbacia = {'BHSF': [],
'BHTOC': []}

#séries de volume com vazão regularizada
volreg = pd.read_csv('seriesvol.csv')

#séries de vazão natural
vaznat = pd.read_csv('vaznat.csv')

#valores de vazão regularizada
vazreg = pd.read_csv('vazoesreg.csv')

t = []
for i in range(1080):
	if i <= 11:
		t.append(mes[i]+'/1931')
	else:
		iano = int(i/12) + 1931
		imes = i % 12
		t.append(mes[imes]+'/'+str(iano))


#####  E A R  #####


#cálculo da cota geométrica
for uhe in cotageo:
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		cotageo[uhe] = [limitecotas[uhe][0] for i in range(1080)]
		#print('UHE: {}:\n'.format(uhe),cotageo[uhe])
	else:
		for i, r in volreg.iterrows():
			cotageo[uhe].append((1/(r[uhe]-limitevol[uhe][0]))*(((pcv[uhe][4]/5)*((r[uhe]**5)-(limitevol[uhe][0]**5)))+((pcv[uhe][3]/4)*((r[uhe]**4)-(limitevol[uhe][0]**4)))+((pcv[uhe][2]/3)*((r[uhe]**3)-(limitevol[uhe][0]**3)))+((pcv[uhe][1]/2)*((r[uhe]**2)-(limitevol[uhe][0]**2)))+((pcv[uhe][0])*((r[uhe])-(limitevol[uhe][0])))))
		#print('UHE {}:\n'.format(uhe),cotageo[uhe])

#cálculo das perdas em retiro baixo para o volume com vazão regularizada
for vol in volreg['retirobaixo']:
	perda['retirobaixo'].append(0.03*(((pcv['retirobaixo'][0])+(pcv['retirobaixo'][1]*vol)+(pcv['retirobaixo'][2]*(vol**2))+(pcv['retirobaixo'][3]*(vol**3))+(pcv['retirobaixo'][4]*(vol**4)))-(cotafuga['retirobaixo'])))

#cálculo da queda líquida equivalente
for uhe in heq:
	for i in range(1080):
		if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
			heq[uhe].append(cotaref[uhe]-cotafuga[uhe]-perda[uhe][i])
		else:
			heq[uhe].append(cotageo[uhe][i]-cotafuga[uhe]-perda[uhe][i])

#cálculo da produtibilidade equivalente
for uhe in prodeq:
	for i in range(1080):
		prodeq[uhe].append(heq[uhe][i]*prodesp[uhe])

#cálculo da EAR
for uhe in EAR:
	if uhe in bhsf:
		#print('O índice da UHE {} na bacia é {}.'.format(uhe, bhsf.index(uhe)))
		pos = bhsf.index(uhe)
		#print('As UHEs após a UHE {} são:'.format(nomes[uhe]))
		for i, r in volreg.iterrows():
			somaprodeq = 0.0
			for item in bhsf[pos+1:]:
				somaprodeq += prodeq[item][i]
				#print('O valor a ser somado devido a UHE {} é {}.'.format(nomes[item],prodeq[item][i]))
			#print('O valor do somatório para a UHE {} no índice {} é: {}.\n'.format(nomes[uhe],i,somaprodeq))
			EAR[uhe].append(((r[uhe]-limitevol[uhe][0])/2.6298)*(prodeq[uhe][i]+somaprodeq))
		#print('A série de EAR para a UHE {} é:\n{}'.format(nomes[uhe],EAR[uhe]))
	else:
		#print('O índice da UHE {} na bacia é {}.'.format(uhe, bhtoc.index(uhe)))
		pos = bhtoc.index(uhe)
		for i, r in volreg.iterrows():
			somaprodeq = 0.0
			for item in bhtoc[pos+1:]:
				somaprodeq += prodeq[item][i]
				#print('O valor a ser somado devido a UHE {} é {}.'.format(nomes[item],prodeq[item][i]))
			#print('O valor do somatório para a UHE {} no índice {} é: {}.'.format(nomes[uhe],i,somaprodeq))
			EAR[uhe].append(((r[uhe]-limitevol[uhe][0])/2.6298)*(prodeq[uhe][i]+somaprodeq))
			#print('O valor da EAR para a UHE {} no índice {} é {}.\n'.format(nomes[uhe],i,((r[uhe]-limitevol[uhe][0])/2.6298)*(prodeq[uhe][i]+somaprodeq)))

#plt.plot(t,EAR['serradamesa'])
#plt.show()

#cálculo da EAR para as bacias
for bacia in EARbacia:
	if bacia == 'BHSF':
		for i in range(1080):
			soma = 0.0
			for uhe in bhsf:
				soma += EAR[uhe][i]
			#if (i == 0) or ((i%12) == 0):
				#print('Ano {}:\n'.format(int(i/12)+1931))
			#print('O valor da EAR na bacia {} no índice {} é: {}\n'.format(bacia,i,soma))
			EARbacia[bacia].append(soma)
	else:
		for i in range(1080):
			soma = 0.0
			for uhe in bhtoc:
				soma += EAR[uhe][i]
			#if (i == 0) or ((i%12) == 0):
				#print('Ano {}:\n'.format(int(i/12)+1931))
			#print('O valor da EAR na bacia {} no índice {} é: {}\n'.format(bacia,i,soma))
			EARbacia[bacia].append(soma)

#cálculo da cota geométrica máxima
for uhe in cotageomax:
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		cotageomax[uhe] = limitecotas[uhe][0]
	else:
		cotageomax[uhe] = (1/(limitevol[uhe][1]-limitevol[uhe][0]))*(((pcv[uhe][4]/5)*((limitevol[uhe][1]**5)-(limitevol[uhe][0]**5)))+((pcv[uhe][3]/4)*((limitevol[uhe][1]**4)-(limitevol[uhe][0]**4)))+((pcv[uhe][2]/3)*((limitevol[uhe][1]**3)-(limitevol[uhe][0]**3)))+((pcv[uhe][1]/2)*((limitevol[uhe][1]**2)-(limitevol[uhe][0]**2)))+((pcv[uhe][0])*((limitevol[uhe][1])-(limitevol[uhe][0]))))
	#print('A cota geométrica máxima da UHE {} é: {}.\n'.format(nomes[uhe],cotageomax[uhe]))

#cálculo da queda líquida equivalente máxima
for uhe in heqmax:
	perdas = 0.0
	if uhe == 'retirobaixo':
		perdas = (0.03*(limitecotas[uhe][1]-cotafuga[uhe]))
	else:
		perdas = perda[uhe][0]
	#print('A perda para a UHE {} é: {}.\n'.format(nomes[uhe],perdas))
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		heqmax[uhe] = cotaref[uhe] - cotafuga[uhe] - perdas
	else:
		heqmax[uhe] = cotageomax[uhe] - cotafuga[uhe] - perdas
	#print('A heqmax para a UHE {} é: {}.\n'.format(nomes[uhe],heqmax[uhe]))

#cálculo da produtibilidade equivalente máxima
for uhe in prodeqmax:
	prodeqmax[uhe] = prodesp[uhe] * heqmax[uhe]
	#print('A produtibilidade equivalente máxima da UHE {} é {}.\n'.format(nomes[uhe],prodeqmax[uhe]))

#cálculo de EAR max
for uhe in prodeqmax:
	somaprodeqmax = 0.0
	if uhe in bhsf:
		pos = bhsf.index(uhe)
		for uhejus in bhsf[pos+1:]:
			somaprodeqmax += prodeqmax[uhejus]
			#print('Valor da soma na UHE {} após a UHE {} é {}.'.format(nomes[uhe],nomes[uhejus],[somaprodeqmax]))
		EARmax[uhe] = ((limitevol[uhe][1]-limitevol[uhe][0])/2.6298)*(prodeqmax[uhe]+somaprodeqmax)
	else:
		pos = bhtoc.index(uhe)
		for uhejus in bhtoc[pos+1:]:
			somaprodeqmax += prodeqmax[uhejus]
			#print('Valor da soma na UHE {} após a UHE {} é {}.'.format(nomes[uhe],nomes[uhejus],[somaprodeqmax]))
		EARmax[uhe] = ((limitevol[uhe][1]-limitevol[uhe][0])/2.6298)*(prodeqmax[uhe]+somaprodeqmax)
	#print('Os parâmetros para UHE {} são:\nVmax - Vmin = {} / prodeqmax = {}/soma = {}.'.format(nomes[uhe],(limitevol[uhe][1]-limitevol[uhe][0]),prodeqmax[uhe],somaprodeqmax))
	#print('EARmax para a UHE {} é {}.\n'.format(nomes[uhe],EARmax[uhe]))


#cálculo de EARmax das bacias
for bacia in EARbaciamax:
	soma = 0.0
	if bacia == 'BHSF':
		for uhe in bhsf:
			soma += EARmax[uhe]
		EARbaciamax[bacia] = soma
	else:
		for uhe in bhtoc:
			soma += EARmax[uhe]
		EARbaciamax[bacia] = soma

#cálculo da proporção de EAR na bacia, em t, em relação à EAR máxima
for bacia in EARbaciamax:
	propEAR[bacia] = []
	for i in range(1080):
		propEAR[bacia].append((EARbacia[bacia][i]/EARbaciamax[bacia])*100)

#cálculo do período crítico para as bacias
for bacia in propEAR:
	#print('\n\nPara a bacia {}:\n'.format(bacia))
	pcs[bacia]['periodos'] = []
	pcs[bacia]['menorvalor'] = []
	pcs[bacia]['periodosconv'] = []
	i = 0
	inic = 0
	periodo = []
	menor = 100.00
	aux = []
	for porc in propEAR[bacia]:
		if porc == 100.00 or porc > 100.00:
			if len(periodo) > 1:
				pcs[bacia]['periodos'].append(periodo[:inic+1])
				pcs[bacia]['menorvalor'].append(menor)
			inic = 0
			menor = porc
			periodo = []
			aux = []
		else:
			if porc < menor:
				try:
					inic = (i - periodo[0])
				except:
					inic += 1
				menor = porc
		periodo.append(i)
		if i == 1079 and porc < 100.00:
			pcs[bacia]['periodos'].append(periodo[:inic+1])
			pcs[bacia]['menorvalor'].append(menor)
		aux.append(i)
		#print('{} -- {:.2f} -- {} -- {} -- {:.2f} -- {}\n'.format(i,porc,inic,periodo,menor,aux[:inic+1]))
		i += 1

#for i in range(len(pcs['menorvalor'])):
	#print('Nº: {} / Menor valor: {:.2f} / Período: {}'.format(i+1,pcs['menorvalor'][i],pcs['periodos'][i]))

#criando lista com nomes para os meses
for bacia in pcs:
	#print('\nPara bacia {}:\n'.format(bacia))
	for p in pcs[bacia]['periodos']:
		#print('\nPeríodo {}, com valor mínimo {:.2f}%:'.format((pcs[bacia]['periodos'].index(p)+1),pcs[bacia]['menorvalor'][pcs[bacia]['periodos'].index(p)]))
		aux = []
		for i in p:
			if i <= 11:
				aux.append(mes[i]+'1931')
			else:
				iano = int(i/12) + 1931
				imes = i % 12
				aux.append(mes[imes]+str(iano))
		#print(aux)
		pcs[bacia]['periodosconv'].append(aux)

#cálculo da vazão média de longo termo
imes, iano = 0, 2
for uhe in heqmax:
	mediaanoqnat[uhe] = []

for i, r in vaznat.iterrows():
	if imes == 0:
		for uhe in heqmax:
			somaano[uhe] = 0.0
		iano += 1
	imes += 1
	for uhe in heqmax:
		if imes in (1,3,5,7,8,10,12):
			somaano[uhe] += r[uhe]*31
		elif imes == 2:
			if iano == 4:
				somaano[uhe] += r[uhe]*29
			else:
				somaano[uhe] += r[uhe]*28
		else:
			somaano[uhe] += r[uhe]*30
	if imes == 12:
		for uhe in heqmax:
			if iano == 4:
				mediaanoqnat[uhe].append((somaano[uhe]/366))
				iano = 0
			else:
				mediaanoqnat[uhe].append((somaano[uhe]/365))
		#for uhe in heqmax:
			#pos = len(mediaanoqnat[uhe]) - 1
			#print('A média anual para a UHE {} é: {} Índice de ano: {}(0 se bissexto)\n'.format(nomes[uhe],mediaanoqnat[uhe][pos],iano))
		imes = 0

for uhe in mediaanoqnat:
	mediaanoqnat[uhe] = sum(mediaanoqnat[uhe]) / 90


#cálculo do grau de regularização:
for uhe in mediaanoqnat:
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		grau[uhe] = 'N/A'
	else:
		for i, r in vazreg.iterrows():
			grau[uhe] = (r[uhe] / mediaanoqnat[uhe])


#####  E N A  #####


#cálculo do volume a 65%
for uhe in limitevol:
	v65 = (0.65*(limitevol[uhe][1]-limitevol[uhe][0])+(limitevol[uhe][0]))
	vol_65[uhe] = v65

#cálculo das cotas com o volume a 65%
for uhe in vol_65:
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		cota_65[uhe] = limitecotas[uhe][0]
	else:
		cota65 = ((pcv[uhe][0])+(pcv[uhe][1]*vol_65[uhe])+(pcv[uhe][2]*(vol_65[uhe]**2))+(pcv[uhe][3]*(vol_65[uhe]**3))+(pcv[uhe][4]*(vol_65[uhe]**4)))
		cota_65[uhe] = cota65

#cálculo da perda a com volume a 65%
for uhe in cota_65:
	if uhe == ' retirobaixo':
		perda_65[uhe] = (0.03*(cota_65[uhe]-cotafuga[uhe]))
	else:
		perda_65[uhe] = perda[uhe][0]

#cálculo da cota geométrica com volume a 65%
for uhe in perda_65:
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		cotageo_65[uhe] = limitecotas[uhe][0]
	else:
		cotageo_65[uhe] = (1/(vol_65[uhe]-limitevol[uhe][0]))*(((pcv[uhe][4]/5)*((vol_65[uhe]**5)-(limitevol[uhe][0]**5)))+((pcv[uhe][3]/4)*((vol_65[uhe]**4)-(limitevol[uhe][0]**4)))+((pcv[uhe][2]/3)*((vol_65[uhe]**3)-(limitevol[uhe][0]**3)))+((pcv[uhe][1]/2)*((vol_65[uhe]**2)-(limitevol[uhe][0]**2)))+((pcv[uhe][0])*((vol_65[uhe])-(limitevol[uhe][0]))))

#cálculo da queda equivalente com volume a 65%
for uhe in cotageo_65:
	if uhe in ('pamx', 'xingo', 'canabrava', 'saosalvador', 'estreito', 'lajeado'):
		heq_65[uhe] = cotaref[uhe] - cotafuga[uhe] - perda_65[uhe]
	else:
		heq_65[uhe] = cotageo_65[uhe] - cotafuga[uhe] - perda_65[uhe]

#cálculo da produtibilidade equivalente com volume a 65%
for uhe in heq_65:
	prodeq_65[uhe] = heq_65[uhe] * prodesp[uhe]

#cálculo da ENA
for uhe in prodeq_65:
	ENA[uhe] = []
	for i, r in vaznat.iterrows():
		ENA[uhe].append(prodeq_65[uhe] * r[uhe])

#print(heq_65['estreito'])
#print(prodeq_65['estreito'])
#print(ENA['estreito'])

#cálculo da ENA das bacias
for i in range(1080):
	valorsf = 0.0
	valortoc = 0.0
	for uhe in ENA:
		if uhe in bhsf:
			valorsf += ENA[uhe][i]
		else:
			valortoc += ENA[uhe][i]
		#print('Valor de ENA para UHE {} no índice {} é {}.'.format(nomes[uhe],(i),ENA[uhe][i]))
		#print('SF = {} após a UHE {} no índice {}.'.format(valorsf,nomes[uhe],i))
		#print('TOC = {} após a UHE {} no índice {}.\n'.format(valortoc,nomes[uhe],i))

	ENAbacia['BHSF'].append(valorsf)
	ENAbacia['BHTOC'].append(valortoc)

#plot
def plotarENA(graf, serie, titulo):
	graf.plot(t,serie)
	graf.xaxis.set_major_locator(plt.MaxNLocator(8))
	graf.set_ylabel('ENA (MWmed)')
	graf.set_title(titulo)

def plotarEAR(graf, serie, titulo):
	graf.plot(t,serie)
	graf.xaxis.set_major_locator(plt.MaxNLocator(8))
	graf.set_ylabel('EAR (MWmed)')
	graf.set_title(titulo)

fig, (graf3, graf4) = plt.subplots(nrows=2, ncols=1)
#plotarENA(graf1, ENAbacia['BHSF'], 'ENA para BHSF')
#plotarENA(graf2, ENAbacia['BHTOC'], 'ENA para BHTOC')
plotarEAR(graf3, propEAR['BHSF'], '%EAR para BHSF')
plotarEAR(graf4, propEAR['BHTOC'], '%EAR para BHTOC')

plt.tight_layout()
plt.show()


