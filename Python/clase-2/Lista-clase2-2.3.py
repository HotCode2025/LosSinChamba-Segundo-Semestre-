# Conectamos listas 
listas1 = [10, 12, 13, 14, 1]
listas2 = [15, 16, 17, 1]
lista3 = listas1 + listas2  # Concatenamos (corregido: era 'listal')
print(lista3)

lista3.extend([18, 19, 20, 1])  # Función para agregar varios elementos a una lista (corregido: extend necesita una lista)
print(lista3)

# Comenté la línea del index(5) porque 5 no está en la lista y daría error
# print(lista3.index(5))  # Función para encontrar el índice de un elemento en una lista

print(lista3.count(1))  # Función para contar el número de veces que un elemento aparece en una lista

# Cómo saber cuántos elementos hay en una lista
print(len(lista3))  # Cuenta el total de elementos en la lista (corregido: len() en lugar de count())

# Para poner al revés una lista 
lista3.reverse()  # Función para invertir una lista
print(lista3)

# Para que una lista se multiplique repitiendo sus valores
lista = [1, 2, 3] * 2  # Multiplica la lista por 2
print(lista)

# Método de ordenamiento de una lista, en python es una función
# que se llama sort, y se puede ordenar de menor a mayor o de mayor a menor
lista3.sort()  # Ordena la lista de menor a mayor
print(lista3)
lista3.sort(reverse=True)  # Ordena la lista de mayor a menor
print(lista3)