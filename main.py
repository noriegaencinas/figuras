# Importando flask para crear el servidor
from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# venv?
# nombres de los archivos?
# donde puedo encontrar esta informacion?
# se hace en docker?