# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud

# Pedir al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Eliminar los espacios de la frase
frase_sin_espacios = frase.replace(" ", "")

# Contar la longitud de la nueva frase
longitud_sin_espacios = len(frase_sin_espacios)

# Imprimir la frase sin espacios y su longitud
print(f"Frase sin espacios: {frase_sin_espacios}")
print(f"Número de caracteres: {longitud_sin_espacios}")
