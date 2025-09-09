# Comenzamos con Funciones
# mi_funcion() # No se puede llamar antes de definir a una funcion

# Definimos una función
def mi_funcion(): # Para identificar a la función utilizamos paréntesis
    print('Saludos a todos lo alumnos de la Tecnicatura')

mi_funcion() # Estamos llamando a la función
mi_funcion() # Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + ' ' + lastName)

    # lista
person = ["Ariel", "Betancud"]

show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función

show(*person) # Esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # desempaquetamos a través de una tupla
show(*person2)

# diccionario
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)
