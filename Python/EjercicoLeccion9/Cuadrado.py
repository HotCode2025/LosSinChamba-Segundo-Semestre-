from FiguraGeometricas import FiguraGeometrica
from Color import Color
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)

        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho


    def __str__(self):
        return f'Cuadrado: {Color.__str__(self)} {FiguraGeometrica.__str__(self)}'