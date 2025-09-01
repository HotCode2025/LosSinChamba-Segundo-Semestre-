#4.4 Ejercicio 1 con Matemáticas y la clase math
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)

# Crear una lista que solo incluya los números menores a 5
# y se imprima por consola [1, 3, 2]

lista = [] # Definimos la lista

# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)

# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
import math

numero = int(input('Digite un numero positivo '))

while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))

print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')