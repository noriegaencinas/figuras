# Importando flask para crear el servidor
from flask import *

app = Flask(__name__)

from controller.menu_controller import *
from controller.circulo_controller import *
from controller.cuadrado_controller import *
from controller.triangulo_controller import *
# from controller.rectangulo_controller import * # Remove this line on deployment

if __name__ == '__main__':
    app.run(port=5085, debug=False, host="0.0.0.0") #Debug true when developing

# DUDAS
# venv?
# nombres de los archivos?
# donde puedo encontrar esta informacion? (de los estandares para nombrar cosas)
# se hace en docker? (en empresas)
# los view se hacen en html?
# los circle svg y eso, es mejor tenerlos en una carpeta o acceder a ellos por internet?
# cada cuanto se hace un commit?