class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un metodo calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """

class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

try:
    ancho_input = float(input("Ingrese el ancho del cubo: "))
    alto_input = float(input("Ingrese el alto del cubo: "))
    profundidad_input = float(input("Ingrese la profundidad del cubo: "))

    mi_cubo = Cubo(ancho_input, alto_input, profundidad_input)

    volumen_cubo = mi_cubo.calcular_volumen()
    print(f"El volumen del cubo es: {volumen_cubo}")

except ValueError:
    print("Entrada no válida. Por favor, ingrese números.")