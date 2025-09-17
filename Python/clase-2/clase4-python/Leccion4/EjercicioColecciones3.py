# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos una lista vacia
# Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(P) # Agregamos a la lista un personaje

P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)

P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)

print(personajes) # Tarea: Agregar por lo menos otros tres personajes, que sean a tu elección

# Ejercicio: Agregar personajes de guerra a una lista
# Creamos una lista vacía para guardar los personajes
personajes = []

# Personaje 1: Sultán Mehmed II (Imperio Otomano)
p1 = {'Nombre': 'Sultán Mehmed II', 'Bando': 'Otomano', 'Rol': 'Conquistador', 'Batalla': 'Caída de Constantinopla'}
personajes.append(p1)

# Personaje 2: Julio César (República Romana)
p2 = {'Nombre': 'Julio César', 'Bando': 'Romano', 'Rol': 'General', 'Batalla': 'Guerra de las Galias'}
personajes.append(p2)

# Personaje 3: Marco Antonio (Imperio Romano)
p3 = {'Nombre': 'Marco Antonio', 'Bando': 'Romano', 'Rol': 'General', 'Batalla': 'Batalla de Accio'}
personajes.append(p3)

# Imprimimos la lista completa para verificar que todo se haya agregado correctamente
print(personajes)

