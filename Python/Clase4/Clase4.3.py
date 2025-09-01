#Ejercicio de Colecciones 3
# Crear una lista vacía para almacenar los personajes
personajes_lotr = []

aragorn = {
    'Nombre': 'Aragon',
    'Clase': 'Guerrero',
    'Raza': 'Dúnadan del norte'
}

gandalf = {
    'Nombre': 'Gandalf',
    'Clase': 'Mago',
    'Raza': 'Istar'
}

legolas = {
    'Nombre': 'Legolas',
    'Clase': 'Arquero',
    'Raza': 'Elfo Sindar'
}

# Añadir los diccionarios a la lista usando .append()
personajes_lotr.append(aragorn)
personajes_lotr.append(gandalf)
personajes_lotr.append(legolas)

# Imprimir la lista completa para verificar el resultado
print("Lista de personajes de El Señor de los Anillos:")
print(personajes_lotr)

print("\n---")

print("Detalle de cada personaje:")
for personaje in personajes_lotr:
    print(f"Nombre: {personaje['Nombre']}")
    print(f"Clase: {personaje['Clase']}")
    print(f"Raza: {personaje['Raza']}")
    print("")