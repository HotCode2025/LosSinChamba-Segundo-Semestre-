#7.2 Argumentos variables para un diccionario
# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    # Se va a convertir en una tupla
    for nombre in nombres:
        print(nombre)

listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy Key')
listarTerminos(Nombre='Leonel Messi')

#7.3 Lista de elementos con funciones (convertir)

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11) # No es un objeto iterable
desplegarNombres((10, 11,)) # La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista