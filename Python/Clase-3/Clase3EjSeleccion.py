# Lista = Ariel, Liliana, Etc
# Colecciones en Python

# Las listas es lo que se conoce en otros lenjuajes como arreglos o vectores
# arreglos

nombres = ["Gabi", "Eze", "Facu", "Lauter", "Lihue", "Mariano", "Kevin", "Lean"]
print(nombres)
print(nombres[0])
print(nombres[3])
print(nombres[-1])  # va de atras hacia al principio
print(nombres[0:8])  # solo muestra el indice 0,1,ect pero no el 8
# Ir al inicio de la lista al indice (sin Incluirlo)
print(nombres[:3])  # indice a mostrar 0,1,2,...
# Desde el indice indicado hasta el final
print(nombres[1:])
# Modificamos un valor
nombres[3] = "Facu"
nombres[4] = "Lauter"
print(nombres)
# Iterar una lista
for nombre in nombres:  # nombre es sing, la lista plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene una lista
print(len(nombres))  # Le pasamos como parametro la lista

#Agregamos un Elemneto
nombres.append("Marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)
# Insereta Elemento en un indice especifico
nombres.insert(1, "Albert")
print(nombres)
nombres.insert(3, "Agus")
print(nombres)
# Eliminar un Elemneto
nombres.remove("Albert")
print(nombres)
#Eliminar el ultimo Elemento
nombres.pop()
print(nombres)
# Eliminar un indice espedifico
del nombres[2]  # del significa delete o eliminar
print(nombres)
#Eliminar, borrar o limpiar todoos los elementos
nombres.clear()
print(nombres)

#Eleminiar la lista
del nombres
#print(nombres)

#Verificamio como trabajar dia dia a Git
#Definimos un Tuplas
cocina = ('cuchara', 'tenedor', ' cuchillo')
print(len(cocina))
# Acceder a un elementro, para utilizamos corchetes no parentesis
print(cocina[0])
#Manera inversa
print(cocina[-1])
#Acceder a un rango
print(cocina[0:1])
#Ejemplos
Juegos = ('cs2',)  #un tupla necesita de un elemnto y la coma (,) si no seria strem o cadena
# Recordemos los elemneto de la Tupla
for cocinar in cocina:  # Print esta usando \n para los saltos de lineas
    print(cocinar, end=' ')  #usamos end= para eliminar los saltos de linea
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)
#del cocina # esto es ara eliminar una tupla

# CLASE 2 2.1
# tipo set
planetas: set[str] = {'Tierra', 'Marte', 'Venus', 'Jupiter'}
print(len(planetas))  # Usamos len para ver cuantos elementos tiene = length significa largo

# Revisar si un elemento existe dentro de set
print('Tierra' in planetas)  # Devuelve True si existe, False si no
print('Saturno' in planetas)  # Devuelve False

# Agregar un elemento al set
planetas.add('Saturno')
planetas.add('tierra')
print(planetas)  # 'tierra' no se agregará porque los sets son únicos

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter")  # Esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard("tierra")  # Esta funcion no nos presenta ningun error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas
#print(planetas)  # al eliminar nos muestra fun error

# 'Leo Messi':10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE': ' Integrated Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}

# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))  # Ahora funcionará correctamente
print(diccionario.get("SABD"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"  # Corregido: era 'diccionarios'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otra manera de acceder a una diccionario
for termino in diccionario.keys():  # Aca estamos usando una funcion
    print(termino)  # Muestra solo las llaves

for termino in diccionario.values():  # Aca usamos la funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario)  # devuelve un booleano

# Agregar un elemento
diccionario["PK"] = "primary key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario  # el diccionario se borro

# Conectamos listas
listas1 = [10, 12, 13, 14, 1]
listas2 = [15, 16, 17, 1]
lista3 = listas1 + listas2  # Concatenamos (corregido: era 'listal')
print(lista3)

lista3.extend(
    [18, 19, 20, 1])  # Función para agregar varios elementos a una lista (corregido: extend necesita una lista)
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

# "Metodo de ordenamiento de una lista, en python es una función"
# que se llama sort, y se puede ordenar de menor a mayor o de mayor a menor
lista3.sort()  # Ordena la lista de menor a mayor
print(lista3)
lista3.sort(reverse=True)  # Ordena la lista de mayor a menor
print(lista3)
# Clase N3
# Repaso de tuplas
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola")  # Pude tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)  #Accion booleano, su respuestas es de tipo booleano
# lo que podemos usar dentro de tupla son: in, not in, index, count
# en tupla se puede convertir de tupla a lista y de lista a tupla
# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #Nos devuelve como respuestas un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto3.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en immutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente immutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)


#Ejercicio Clases3 Presentar SeleccionArg.

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 28, 'Altura': 1.80, 'Precio': '30 Millones', 'Posicion': 'Centrocampista'},
    23: {'Nombre': 'Emiliano Martínez', 'Edad': 30, 'Altura': 1.95, 'Precio': '28 Millones', 'Posicion': 'Portero'},
    9: {'Nombre': 'Julián Álvarez', 'Edad': 22, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Delantero Centro'},
    22: {'Nombre': 'Lautaro Martínez', 'Edad': 25, 'Altura': 1.74, 'Precio': '75 Millones', 'Posicion': 'Delantero Centro'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.76, 'Precio': '42 Millones', 'Posicion': 'Centrocampista'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 25, 'Altura': 1.75, 'Precio': '20 Millones', 'Posicion': 'Lateral Derecho'},
    21: {'Nombre': 'Enzo Fernández', 'Edad': 21, 'Altura': 1.78, 'Precio': '85 Millones', 'Posicion': 'Centrocampista'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 Jugadores mas al diccionario: seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedó así: {pila}')
# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)