# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.
# Definimos una función
def sumar_valor(*args): # Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

# Llamamos a la función
print(sumar_valor(3, 5, 9, 2, 1))

#Trababo realizado por Alumnos
# Definimos la función 'sumar_numeros'.
# que recoja todos los argumentos que le pasemos y los guarde en una tupla.
def sumar_numeros(*numeros):
    total = 0
    for numero in numeros:

        total += numero

    return total
# Ahora, probamos la función llamándola con diferentes cantidades de números.
print(f'La suma es: {sumar_numeros(5, 10, 15)}')
print(f'La suma es: {sumar_numeros(10, 20, 30, 40, 50)}')
print(f'La suma es: {sumar_numeros(1, 2, 3)}')