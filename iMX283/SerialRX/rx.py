import serial
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)


while (1):
	dato = SAM3S.readline()
	print(dato)

#SAM3S.close()
