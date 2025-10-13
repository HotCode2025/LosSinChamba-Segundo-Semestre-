"""
Definir una clase padre llamada Vehículo y dos clases hijas llamadas
Auto y Bicicleta, las cuales heredan de la clase padre Vehículo. La clase
padre debe tener los siguientes atributos y métodos:

Vehiculo (clase padre)
-Atributos(color, ruedas)
-Métodos(__init__(), y __str__())

-Auto (clase hija de Vehículo)
-Atributos(velocidad (km/hr))
-Métodos(__init__(color, ruedas, velocidad), y __str__())

Bicicleta (clase hija de Vehículo)
-Atributos(tipo(urbana/montaña/etc.))
-Métodos(__init__(colo, ruedas, tipo), y __str__())

Crear un objeto de cada clase
"""
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"Auto -> {super().__str__()}, Velocidad: {self.velocidad} km/h"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta -> {super().__str__()}, Tipo: {self.tipo}"



vehiculo1 = Vehiculo("Gris", 4)
auto1 = Auto("Rojo", 4, 180)
bicicleta1 = Bicicleta("Azul", 2, "Montaña")

# Impresión de objetos (llama automáticamente a __str__)
print(vehiculo1)
print(auto1)
print(bicicleta1)