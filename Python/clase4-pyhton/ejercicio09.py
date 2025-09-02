frase = input("Ingresa una frase: ")

frase_sin_espacios = frase.replace(" ", "")

contador_caracteres = len(frase_sin_espacios)

print(f"Frase original: {frase}")
print(f"Frase sin espacios: {frase_sin_espacios}")
print(f"Número de caracteres (sin espacios): {contador_caracteres}")