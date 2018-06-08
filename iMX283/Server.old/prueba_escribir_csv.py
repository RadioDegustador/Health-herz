import csv, time, os

datos = [0,0.1,0.2,0.3,0.4]

while(1):
	datos_s = []
	datos1 = []
	os.remove('./datos.csv')
	for elemento in datos:
		datos1.append(elemento*1.2)
		elemento = str(elemento)
		datos_s.append(elemento)
	print(datos_s)
	datos = datos1
	myFile = open('datos.csv','w')
	with myFile:
	      writer = csv.writer(myFile)
	      writer.writerows([datos_s])
	time.sleep(10)
