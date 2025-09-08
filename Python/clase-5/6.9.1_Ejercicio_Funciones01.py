# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos

def sumar_valores(*args):
    """
    Función que suma todos los valores numéricos recibidos como argumentos
    Args:
        *args: argumentos variables de tipo numérico
    Returns:
        La suma de todos los valores pasados como argumentos
    """
    return sum(args)

# Ejemplos de uso
def main():
    print("=== EJEMPLOS DE USO ===")
    
    # Ejemplo 1: Sin argumentos
    resultado1 = sumar_valores()
    print(f"sumar_valores() = {resultado1}")
    
    # Ejemplo 2: Un solo argumento
    resultado2 = sumar_valores(5)
    print(f"sumar_valores(5) = {resultado2}")
    
    # Ejemplo 3: Varios argumentos enteros
    resultado3 = sumar_valores(1, 5, 3, 4, 8)
    print(f"sumar_valores(1, 2, 5, 4, 8) = {resultado3}")
    
    # Ejemplo 4: Argumentos decimales
    resultado4 = sumar_valores(1.5, 2.5, 4.5)
    print(f"sumar_valores(1.5, 2.5, 4.5) = {resultado4}")
    
    # Ejemplo 5: Mezcla de enteros y decimales
    resultado5 = sumar_valores(10, 20.5, 15, 7.2, 3)
    print(f"sumar_valores(10, 20.5, 15, 7.2, 3) = {resultado5}")
    
    # Ejemplo 6: Números negativos
    resultado6 = sumar_valores(-5, 10, -3, 8)
    print(f"sumar_valores(-5, 10, -3, 8) = {resultado6}")

if __name__ == "__main__":
    main()