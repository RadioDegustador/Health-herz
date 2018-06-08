from flask import Flask, render_template
import json
import serial
import csv
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
#SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)

datos = []
eje = []
bpm = 60
Ts = 0.004

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    	datos = []
    	eje = []
    	with open('./datos.csv') as File:
    		reader = csv.reader(File,delimiter=',')
		for row in reader:
			for elemento in row:
				elemento = int(elemento)
				datos.append(elemento)
	
	prom = 0.0
	for idx in range(0,len(datos)):
		prom=prom+datos[idx]
	
	prom = prom/len(datos)

	num_max = max(datos)

	for i in range(0,len(datos)):
		eje.append(i)
		datos[i] = (datos[i]-prom)/num_max

	#Calculo de los latidos por minuto
	for i in range(0,len(datos)):
		if(datos[i]>0.75):
			flag1 = i
			break
			
	for i in range(flag1+int(0.2/Ts),len(datos)):
		if(datos[i]>0.75):
			flag2 = i
			break
		
	bpm = int(60/((flag2-flag1)*Ts))

    	return render_template('graph.html', datos = datos, eje = eje, bpm = str(bpm))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
