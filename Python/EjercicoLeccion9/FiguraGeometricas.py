class FiguraGeometrica:
    def __init__(self, alto, ancho):

        self._alto = alto
        self._ancho = ancho


    def get_alto(self):
        return self._alto

    def get_ancho(self):
        return self._ancho

    def set_alto(self, alto):
        self._alto = alto

    def set_ancho(self, ancho):
        self._ancho = ancho

    # Metodo para representar el objeto como cadena
    def __str__(self):
        return f'FiguraGeometrica [Alto: {self._alto}, Ancho: {self._ancho}]'

