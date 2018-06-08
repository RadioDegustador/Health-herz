from flask import Flask, render_template
import json
import serial
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
	SAM3S.flushInput()
	while (i<800):
		dato = SAM3S.readline()
		try:
			dato_float = -1*float(dato)
			senal.append(max(0,min(dato_float,303508)))
			print(i)
			print(dato_float)
		except ValueError:
			senal.append(senal[len(senal)-1])
			print('Error')
		i = i + 1

	SAM3S.close()
	
	prom = 0.0
	for idx in range(0,len(senal)):
		prom=prom+senal[idx]
	
	prom = prom/len(senal)

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

    	return render_template('graph.html', datos = senal, eje = eje, bpm = str(bpm))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
