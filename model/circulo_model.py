import math # Libreria para trabajar con funciones matemáticas
import figura_geometrica_model # Importamos la clase FiguraGeometrica del archivo figura_geometrica_model.py

class Circulo(figura_geometrica_model.FiguraGeometrica): # Creamos la clase Circulo que hereda de FiguraGeometrica
    def __init__(self, radio):
        self.radio = radio 

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio