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
