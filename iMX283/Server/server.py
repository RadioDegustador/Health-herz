from flask import Flask, render_template

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/graph', methods =['GET', 'POST'])
def send():
    return render_template ('graph.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
