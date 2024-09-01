import math # Libreria para trabajar con funciones matemáticas
from model.figura_geometrica_model import FiguraGeometrica# Importamos la clase FiguraGeometrica del archivo figura_geometrica_model.py

class Circulo(FiguraGeometrica): # Creamos la clase Circulo que hereda de FiguraGeometrica    

    def __init__(self, radio):
        self.radio = radio         
        self.image = 'static/circle.svg' # Image of the circle
        self.name = 'Circulo'

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio