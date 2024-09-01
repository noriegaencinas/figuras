# Importando flask para crear el servidor
from flask import *

app = Flask(__name__)

from controller.menu_controller import *
from controller.circulo_controller import *
from controller.cuadrado_controller import *
from controller.triangulo_controller import *

if __name__ == '__main__':
    app.run(port=5013, debug=False) #Debug true when developing

# DUDAS
# venv?
# nombres de los archivos?
# donde puedo encontrar esta informacion? (de los estandares para nombrar cosas)
# se hace en docker? (en empresas)
# los view se hacen en html?
# los circle svg y eso, es mejor tenerlos en una carpeta o acceder a ellos por internet?
# cada cuanto se hace un commit?