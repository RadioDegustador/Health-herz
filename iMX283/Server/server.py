from flask import Flask, render_template
import json
import serial
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
#SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)
#datos = []

#while (1):
#	dato = SAM3S.readline()
##	print(dato)

#SAM3S.close()
app  = Flask(__name__)

#eje = []
#x = len(datos)

#for i in range(x):
#    nuevodato = i+1
#    eje.append(nuevodato)

eje = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
datos = [1,1,0,0,1,1,0,0,1,1,0,0]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    arreglodatos = datos
    return render_template('graph.html', datos = datos, eje = eje)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
