import serial, threading, time, os, csv
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)

def lectura():
	global senal,i
	senal = []
	i = 0
	for idx in range(1,81):
		senal.append(0)
	while (1):
		dato = SAM3S.readline()
		dato_float = round(float(dato)/1000,3)
		dato_int = int(dato_float)
		senal.append(dato_int)
		i = i + 1

	SAM3S.close()
	
def escritura():
	global senal, i
	time.sleep(1)
	while(1):
		if i >= 20:
			datos_s = []
			os.remove('/media/datos.csv')
			for elemento in senal:
				elemento = str(elemento)
				datos_s.append(elemento)
			myFile = open('/media/datos.csv','w')
			with myFile:
				writer = csv.writer(myFile)
			 	writer.writerows([datos_s])
			print('Se guardaron los datos')
			myFile.close
			senal = senal[len(senal)-80:len(senal)]
			i = 0
		time.sleep(0.26)
		
thread1 = threading.Thread(target=lectura)
thread2 = threading.Thread(target=escritura)

thread1.start()
thread2.start()
