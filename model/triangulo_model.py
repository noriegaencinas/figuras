from model.figura_geometrica_model import FiguraGeometrica # Importamos la clase FiguraGeometrica del archivo figura_geometrica_model.py

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.image = 'static/triangle.svg' # Image of the triangle
        self.name = 'Triangulo'

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base * 3