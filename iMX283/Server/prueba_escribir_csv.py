import csv, time, os, serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)

senal = [0,0,0,0,0]

while(1):
	datos_s = []
	datos1 = []
	os.remove('datos.csv')
	for elemento in datos:
		datos1.append(elemento*2)
		elemento = str(elemento)
		datos_s.append(elemento)
	print(datos_s)
	datos = datos1
	myFile = open('datos.csv','w')
	with myFile:
	      writer = csv.writer(myFile)
	      writer.writerows([datos_s])
	time.sleep(10)
