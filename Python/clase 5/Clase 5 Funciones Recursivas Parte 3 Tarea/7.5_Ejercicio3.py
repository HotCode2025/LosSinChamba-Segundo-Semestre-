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

def imprimir_descendente(numero):
    """
    Función recursiva que imprime números de forma descendente desde 
    el número dado hasta 1.
    
    Args:
        numero (int): Número desde el cual comenzar la cuenta descendente
    
    Returns:
        None: Esta función solo imprime, no retorna valores
    """
    # Caso base: si el número es menor o igual a 0, no imprime nada
    if numero <= 0:
        return
    
    # Imprime el número actual
    print(numero)
    
    # Llamada recursiva con el número decrementado en 1
    imprimir_descendente(numero - 1)


def imprimir_descendente_con_mensaje(numero):
    """
    Versión alternativa que incluye mensajes informativos
    """
    if numero <= 0:
        print("No se imprimen números negativos o cero")
        return
    
    print(f"Contando desde {numero}:")
    imprimir_descendente(numero)
    print("¡Terminado!")


# Ejemplos de uso y pruebas
if __name__ == "__main__":
    print("=== Ejercicio 3: Función Recursiva ===")
    print()
    
    # Ejemplo 1: Número 5
    print("Ejemplo 1 - Número 5:")
    imprimir_descendente(5)
    print()
    
    # Ejemplo 2: Número 3
    print("Ejemplo 2 - Número 3:")
    imprimir_descendente(3)
    print()
    
    # Ejemplo 3: Número 1
    print("Ejemplo 3 - Número 1:")
    imprimir_descendente(1)
    print()
    
    # Ejemplo 4: Número 0 (no imprime nada)
    print("Ejemplo 4 - Número 0:")
    imprimir_descendente(0)
    print("(No se imprimió nada)")
    print()
    
    # Ejemplo 5: Número negativo (no imprime nada)
    print("Ejemplo 5 - Número negativo (-2):")
    imprimir_descendente(-2)
    print("(No se imprimió nada)")
    print()
    
    # Ejemplo 6: Número más grande
    print("Ejemplo 6 - Número 7:")
    imprimir_descendente(7)
    print()
    
    # Usando la versión con mensajes
    print("=== Versión con mensajes informativos ===")
    imprimir_descendente_con_mensaje(4)
    print()
    imprimir_descendente_con_mensaje(-1)