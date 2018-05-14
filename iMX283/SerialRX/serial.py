import serial #Libreria para usar el puerto serial
import time

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=9600,timeout = 3.0)

while True
	dato = SAM3S.readline()
	print(dato)

SAM3S.close()
