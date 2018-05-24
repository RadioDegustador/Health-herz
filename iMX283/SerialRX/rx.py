import serial
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)

senal = [0,0,0,0,0]
eje = [-5,-4,-3,-2,-1,0]

while (1):
	dato = SAM3S.readline()
	dato_float = round(float(dato[0:4])/1000,3) 
	senal = [senal[1],senal[2],senal[3],senal[4],dato_float]
	print(senal)
	print(dato)

SAM3S.close()
