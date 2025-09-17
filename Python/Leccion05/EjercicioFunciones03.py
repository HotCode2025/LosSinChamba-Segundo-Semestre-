# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1:  # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero - 1)  # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

imprimir_numeros_recursivos(1) # Tarea: que el número lo ingrese el usuario


#Tarea

def imprimir_numeros_recursivos(numero):
    """
    Imprime números de forma descendente usando una función recursiva.
    """
    if numero < 1:

        return
    else:

        print(numero)
        imprimir_numeros_recursivos(numero - 1)

# Ejemplos de uso según el ejercicio:
print("Imprimiendo desde 5:")
imprimir_numeros_recursivos(5)
print("\nImprimiendo desde 3:")
imprimir_numeros_recursivos(3)
print("\nProbando con un número negativo:")
imprimir_numeros_recursivos(-2)