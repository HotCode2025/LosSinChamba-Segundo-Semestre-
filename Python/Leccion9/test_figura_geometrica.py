from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'Azul')

print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

#MRO = metodo de resolucion de orden
print(Cuadrado.mro())