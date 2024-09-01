from model.figura_geometrica_model import FiguraGeometrica# Importamos la clase FiguraGeometrica del archivo figura_geometrica_model.py

class Cuadrado(FiguraGeometrica): # Creamos la clase Cuadrado que hereda de FiguraGeometrica
    def __init__(self, lado):
        self.lado = lado
        self.image = 'static/square.svg' # Image of the square
        self.name = 'Cuadrado'
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return self.lado * 4
        