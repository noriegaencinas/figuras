from abc import ABC, abstractmethod # Python necesita importar la librería ABC y abstractmethod para poder trabajar con clases abstractas

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass