import serial
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)


while (1):
	dato = SAM3S.readline()
	print(dato)

#SAM3S.close()

from flask import Flask, render_template
import json

app  = Flask(__name__)

eje = []
x = len(dato)

for i in range(x):
    nuevodato = i+1
    eje.append(nuevodato)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    datos = dato
    return render_template('graph.html', datos = datos, eje = eje)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
