# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor

# Creamos una lista vacía para almacenar los números
lista = []

# Bucle para pedir números al usuario
while True:
    numero = int(input('Digite un número (ingrese 0 para salir): '))
    if numero == 0:
        break
    lista.append(numero)

# Ordenamos la lista de menor a mayor
lista.sort()

# Imprimimos la lista ordenada
print("Los números ordenados son:", lista)