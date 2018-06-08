from flask import Flask, render_template
import json
import serial
import nympy as np
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
#SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)

datos = []
eje = []
bpm = 60

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    	senal = []
    	eje = []
    
    	#El puerto al que esta conectado el SAM3S es /dev/ttySP0
	SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)
	i = 0
	while (i<1200):
		dato = SAM3S.readline()
		flag = 0
		for idx in range(0,len(dato)):
                	if(dato[idx]==','):
				try:			
					senal.append(int(dato[flag:idx])) 
				except ValueError:
					senal.append(0)
					print('Error en la trama')
		flag = idx+1
        	try:
			senal.append(int(dato[flag:len(dato)]))
		except ValueError:
			senal.append(0)
			print('Error en la trama')
		i = i + 12

	SAM3S.close()
	SAM3S.reset_input_buffer()
	
	for i in range(0,len(senal)):
		eje.append(i)

    	return render_template('graph.html', datos = senal, eje = eje, bpm = str(bpm))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
