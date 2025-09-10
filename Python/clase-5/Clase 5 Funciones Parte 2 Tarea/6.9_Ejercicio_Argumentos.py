# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres:
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')