# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres


# Pedir la cadena al usuario
cadena = input("Ingresa una cadena de texto por teclado: ")
    
# Crear una lista vacía para almacenar caracteres únicos
caracteres_unicos = []
    
# Recorrer cada carácter de la cadena
for caracter in cadena:
    # Solo agregar el carácter si no está ya en la lista
    if caracter not in caracteres_unicos:
        caracteres_unicos.append(caracter)
            
# Mostrar el resultado
print(f"Cadena original: '{cadena}'")
print(f"Caracteres únicos: {caracteres_unicos}")
#    print(f"Total de caracteres únicos: {len(caracteres_unicos)}")
