#7.4 Funciones recursivas con factorial
# Funciones Recursivas
def factorial(numero):

    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo

resultado = factorial(5) # Lo hacemos en código duro

print(f'El factorial del número 5 es: {resultado}')

# Tarea que el usuario ingrese el numero para calcular el factorial


# --- Función Recursiva ---
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
numero_fijo = 8
resultado = factorial(numero_fijo)
print(f'El factorial del número {numero_fijo} es: {resultado}')

# --- Función Recursiva ---
# La función no cambia, sigue la misma lógica.
def factorial(numero):

    # Caso Base: si el número es 0 o 1, su factorial es 1.
    if numero == 0 or numero == 1:
        return 1
    # Caso Recursivo: el número multiplicado por el factorial del número anterior.
    else:
        return numero * factorial(numero - 1)

# --- Ejemplo 2 de la tarea ---
# Pedimos al usuario que ingrese un número.
# int() convierte la entrada (que es texto) a un número entero.
try:
    numero_ingresado = int(input("Ingresa un número entero para calcular su factorial: "))
    if numero_ingresado < 0: # Verificamos que no sea un número negativo.
        print("Error: El factorial no está definido para números negativos.")
    else:
        resultado = factorial(numero_ingresado) # Llamamos a la función con el número del usuario.
        print(f"El factorial de {numero_ingresado} es: {resultado}")    # Mostramos el resultado.
except ValueError:
    print("Error: Debes ingresar un número entero válido.")  # Este bloque se ejecuta si el usuario

                                                             # ingresa algo que no es un número.
