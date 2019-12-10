from flask import Flask

app = Flask(__name__)

@app.route('/')
def index1():
    return 'Ciao!'

@app.route('/pagina/')
def index2():
    return 'Pagina!'

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
