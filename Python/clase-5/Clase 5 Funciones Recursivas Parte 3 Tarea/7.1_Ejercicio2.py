# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos

def multiplicar(*args):
    """
    Función que multiplica todos los argumentos numéricos pasados.
    
    Args:
        *args: Argumentos variables de tipo numérico
        
    Returns:
        El producto de todos los argumentos, o 1 si no hay argumentos
    """
    # Si no hay argumentos, retornamos 1 (elemento neutro de la multiplicación)
    if not args:
        return 1
    
    # Inicializamos el resultado con 1
    resultado = 1
    
    # Multiplicamos cada argumento
    for numero in args:
        # Verificamos que sea un número
        if isinstance(numero, (int, float)):
            resultado *= numero
        else:
            print(f"Advertencia: {numero} no es un número válido, se omite.")
    
    return resultado

# Ejemplos de uso:
if __name__ == "__main__":
    # Pruebas con diferentes cantidades de argumentos
    print("Ejemplos de uso:")
    print(f"multiplicar(2, 3, 4) = {multiplicar(2, 3, 4)}")  # 24
    print(f"multiplicar(5) = {multiplicar(5)}")  # 5
    print(f"multiplicar(2.5, 4) = {multiplicar(2.5, 4)}")  # 10.0
    print(f"multiplicar() = {multiplicar()}")  # 1
    print(f"multiplicar(1, 2, 3, 4, 5) = {multiplicar(1, 2, 3, 4, 5)}")  # 120
    print(f"multiplicar(-2, 3) = {multiplicar(-2, 3)}")  # -6
    
    # Prueba con tipos no numéricos
    print(f"multiplicar(2, 'texto', 3) = {multiplicar(2, 'texto', 3)}")  # 6 con advertencia