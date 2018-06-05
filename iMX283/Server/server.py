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

    for i in range(len(datos)):
	eje.append(i+1)

    return render_template('graph.html', datos = datos, eje = eje, bpm = str(bpm))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
