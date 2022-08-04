pcv = [3.914048e02,2.77216e-03,-4.35725e-08,2.90304e-13,0.0]
pac = [1.59666e05,-9.862449e02,1.94994,-1.20015e-03,0.0]

vmax = 54400.00
vmin = 11150.00
vol = vmax

qnat = [1049,1426,2515,1604]
eva = [27,8,16,26]

for i in range(4):
	cota = pcv[0] + (pcv[1] * vol) + (pcv[2] * (vol**2)) + (pcv[3] * (vol**3)) + (pcv[4] * (vol**4))
	area = pac[0] + (pac[1] * cota) + (pac[2] * (cota**2)) + (pac[3] * (cota**3)) + (pac[4] * (cota**4))
	evap = (eva[i] * area)/1000
	vol = vol - evap + ((qnat[i] - 591) * 2.6784)
	if vol > vmax:
		vol = vmax
	print(cota,area,vol)