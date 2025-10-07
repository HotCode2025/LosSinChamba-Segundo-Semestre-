class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo será calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
rectangulos = []

for i in range(3):
    print(f"\nIngrese los valores para el rectangulo #{i + 1}:")
    try:
        base_input = float(input("Ingrese la base: "))
        altura_input = float(input("Ingrese la altura: "))


        nuevo_rectangulo = Rectangulo(base_input, altura_input)
        rectangulos.append(nuevo_rectangulo)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese números.")
print("\n--- Resultados ---")
for i, rectangulo in enumerate(rectangulos):
    area = rectangulo.calcular_area()
    print(f"El área del rectangulo #{i + 1} es: {area}")