# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

# Creamos la lista inicial con los números del 1 al 10
lista = list(range(1, 11))

# Solicitamos al usuario que ingrese un valor para multiplicar
valor = int(input('Ingrese un valor para multiplicar los elementos de la lista: '))

# Modificamos los elementos de la lista en su lugar (in-place)
for i in range(len(lista)):
    lista[i] *= valor

# Imprimimos la lista modificada
print(lista)