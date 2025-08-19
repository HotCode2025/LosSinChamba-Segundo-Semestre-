# conectamos lista 
listas1 = [10, 12, 13, 14, 1]
listas2 = [15, 16, 17, 1]
lista3 = listal+listas2 # concatenamos
print(lista3)

lista3.extend(18, 19, 20, 1) # Funcion para agregar varios elementos a una lista 
print(lista3)


print(lista3.index(5)) # Funcion para encontrar el indice de un elemento en una lista
print(lista3.count(1)) # Funcion para contar el numero de veces que un elemento aparece en una lista

# Como saber cuantos elementos hay en una lista
print(lista3.count(1))) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista 
lista3.reverse() # Funcion para invertir una lista
print(lista3)

# Para que una lista se multiplique repitiendo sus valores
lista = [1, 2, 3] * 2 # Multiplica la lista por 2
print(lista)

# Metodo de ordenamiento de una lista, en pyhton es una funcion
# que se llama sort, y se puede ordenar de menor a mayor o de mayor a menor
lista3.sort() # Ordena la lista de menor a mayor
print(lista3)
lista3.sort(reverse=True) # Ordena la lista de mayor a menor
print(lista3)
