import serial
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200)

while (1):
        senal = []
        dato = SAM3S.readline()
        flag = 0
        for i in range(0,len(dato)):
                if(dato[i]==','):
                        senal.append(int(dato[flag:i]))
                        flag = i+1
        senal.append(int(dato[flag:len(dato)]))
        print(senal)
        print(dato)

SAM3S.close()
