# Lista = Gabi,Eze,Facu,Lauter,Lihue,Mariano,Kevin y Lean
 



nombres= ["Gabi","Eze","Facu","Lauter","Lihue","Mariano","Kevin","Lean"]
print(nombres)
print(nombres[0])
print(nombres[3])
print(nombres[-1]) # va de atras hacia al principio
print(nombres[0:8])#solo muestra el indice 0,1,ect pero no el 8
#Ir al inicio de la lista al indice (sin Incluirlo)
print(nombres[ :3]) #indice a mostrar 0,1,2,...
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[3] = "Facu"
nombres[4] = "Lauter"
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es sing, la lista plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene una lista
print(len(nombres)) # Le pasamos como parametro la lista

#Agregamos un Elemneto
nombres.append("Marcelo")
print(nombres)
# Insereta Elemento en un indice especifico
nombres.insert( 1, "Albert")
print(nombres)
nombres.insert( 3,  "Agus")
print(nombres)
# Eliminar un Elemneto
nombres.remove("Albert")
print(nombres)
#Eliminar el ultimo Elemento
nombres.pop()
print(nombres)
# Eliminar un indice espedifico
del nombres [2]# del significa delete o eliminar
print(nombres)
#Eliminar, borrar o limpiar todoos los elementos
nombres.clear()
print(nombres)

#Eleminiar la lista
del nombres
#print(nombres)

#Verificamio como trabajar dia dia a Git
#Definimos un Tuplas
cocina = ('cuchara','tenedor', ' cuchillo')
print(len(cocina))
# Acceder a un elementro, para utilizamos corchetes no parentesis
print(cocina[0])
#Manera inversa
print(cocina[-1])
#Acceder a un rango
print(cocina[0:1])
#Ejemplos
Juegos = ('cs2',)#un tupla necesita de un elemnto y la coma (,) si no seria strem o cadena
# Recordemos los elemneto de la Tupla

for cocinar in cocina:# Print esta usando \n para los saltos de lineas
   print(cocinar, end= ' ') #usamos end= para eliminar los saltos de linea
cocinaLista = list (cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n' , cocina)
#del cocina




# CLASE 2 2.1
# tipo set
planetas = {'Tierra', 'Marte', 'Venus', 'Jupiter'}
print(len(planetas)) # Usamos len para ver cuantos elementos tiene = length significa largo 

# Revisar si un elemento existe dentro de set 
print('Tierra' in planetas)  # Devuelve True si existe, False si no
print('Saturno' in planetas)  # Devuelve False

# Agregar un elemento al set
planetas.add('Saturno')
planetas.add('tierra')
print(planetas)  # 'tierra' no se agregará porque los sets son únicos

# Eliminar elementos, puede arrojar un error si el elemento no existe 
planetas.remove("Jupiter") # Esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard("tierra") # Esta funcion no nos presenta ningun error 
print(planetas)

# Limpiar set 
planetas.clear()
print(planetas)

# Eliminar set 
del planetas 
print(planetas) # al eliminar nos muetra fun error 





# CLASE 2 2.2
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
for termino, valor in diccionario.keys(): # Aca estamos usando una funcion
    print(termino) # Muestra solo las llaves 

for termino, valor in diccionario.values(): # Aca usamos la funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento 
print ("IDE" in diccionario) # devuelve un booleano 

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
del diccionario # el diccionario se borro 





#CLASE 3 2.3
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




#CLASE 2 2.4
# Repaso de tuplas 
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola") # Pude tener diferentes tipos de datos dentro 
print(tupla)

orint(4 in tupla) #Accion booleano, su respuestas es de tipo booleano
# lo que podemos usar dentro de tupla son: in, not in, index, count
# en tupla se puede convertir de tupla a lista y de lista a tupla 

