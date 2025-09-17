# Ejercicio 2: Función con *args para multiplicar // 7.1
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumento
# Definimos la función 'multiplicar_valores' que recibe un número variable de argumentos
# usando el parámetro *args.
def multiplicar_valores(*args):
    if not args:
        return 0
    resultado = 1
    for numero in args:

        resultado *= numero
    return resultado

# --- Ejemplos de uso ---
# Ejemplo 1: Multiplicar 3 números
multiplicacion1 = multiplicar_valores(5, 10, 2)
print(f"El resultado de la multiplicación de 5, 10 y 2 es: {multiplicacion1}")

# Ejemplo 2: Multiplicar 4 números
multiplicacion2 = multiplicar_valores(3, 4, 5, 2)
print(f"El resultado de la multiplicación de 3, 4, 5 y 2 es: {multiplicacion2}")

# Ejemplo 3: Multiplicar un solo número
multiplicacion3 = multiplicar_valores(7)
print(f"El resultado de la multiplicación de 7 es: {multiplicacion3}")

# Ejemplo 4: Llamar a la función sin argumentos
multiplicacion4 = multiplicar_valores()
print(f"El resultado de la multiplicación sin argumentos es: {multiplicacion4}")

