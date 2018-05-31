from flask import Flask, render_template
import json
import serial
import csv
#Libreria para usar el puerto serial

#El puerto al que esta conectado el SAM3S es /dev/ttySP0
#SAM3S = serial.Serial('/dev/ttySP0',baudrate=115200,timeout = 3.0)

datos = [0,0,0,0,0]
eje = [-5,-4,-3,-2,-1,0]

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    datos = []
    with open('./datos.csv') as File:
        reader = csv.reader(File,delimiter=',')
        print(reader)
        for row in reader:
           for elemento in row:
              elemento = int(elemento)
              datos.append(elemento)
        
    print(datos)
    return render_template('graph.html', datos = datos, eje = eje)

@app.route('/graph2', methods =['GET', 'POST'])
def send2():
    datos = [1,0,1,0,1]
    print('Flag 2')
    return render_template('graph.html', datos = datos, eje = eje)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
