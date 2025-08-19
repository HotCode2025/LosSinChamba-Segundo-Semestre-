# Lista = Ariel, Liliana, Etc

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
