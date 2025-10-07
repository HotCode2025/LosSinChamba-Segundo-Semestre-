from FiguraGeometricas import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)

        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Rectangulo: {Color.__str__(self)} {FiguraGeometrica.__str__(self)}'