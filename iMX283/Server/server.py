from flask import Flask, render_template
import json

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    datos = [5, 2, 4, 2, 5]
    return render_template('graph.html', datos = datos)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
