from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('--- ORDEN DE RESOLUCIÓN DE MÉTODOS (MRO) ---')
print(f'MRO de Cuadrado: {Cuadrado.__mro__}')
print(f'MRO de Rectangulo: {Rectangulo.__mro__}')
print('-' * 45)

print('--- Creación de Cuadrado ---')
cuadrado1 = Cuadrado(lado=8, color='Rojo')

print(cuadrado1)

area_cuadrado = cuadrado1.calcular_area()
print(f'Área del cuadrado: {area_cuadrado}')
print('-' * 45)

print('--- Modificando Cuadrado ---')
cuadrado1.set_ancho(10)
cuadrado1.set_color('Naranja')
print(f'Nuevo ancho: {cuadrado1.get_ancho()}')
print(f'Nuevo color: {cuadrado1.get_color()}')
print(cuadrado1)
print('-' * 45)


print('--- Creación de Rectángulo ---')
rectangulo1 = Rectangulo(alto=10, ancho=5, color='Verde')

print(rectangulo1)

area_rectangulo = rectangulo1.calcular_area()
print(f'Área del rectángulo: {area_rectangulo}')
print('-' * 45)

print('--- Modificando Rectángulo ---')
rectangulo1.set_alto(15)
print(f'Nuevo alto: {rectangulo1.get_alto()}')
print(rectangulo1)
print('-' * 45)