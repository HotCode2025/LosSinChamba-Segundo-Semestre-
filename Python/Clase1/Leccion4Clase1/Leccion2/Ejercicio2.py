# Ejercicio 1: Expresión Algorítmica Clase 6 PowerPoint

# 1. Pedimos al usuario 3 valores: a, b, c
# Usamos float() para permitir que el usuario ingrese números con decimales.
# a = float(input('Digite el valor de a: '))
# b = float(input('Digite el valor de b: '))
# c = float(input('Digite el valor de c: '))
#
# # Calculamos el resultado usando la expresión matemática.
# # En Python, la potencia se escribe con ** (ej: a**3 es a al cubo)
# # y la multiplicación con *
# resultado = (a**3 * (b**2 - 2 * a * c)) / (2 * b)
#
# # 2. Mostramos el resultado final
# # Usamos un f-string para formatear la salida de una manera clara.
# print(f'El resultado de la expresión es: {resultado}')

# Ejercicio 2: Solución Lógica

# Pedimos al usuario los valores de a y b
# a = float(input('Digite el valor de a: '))
# b = float(input('Digite el valor de b: '))
#
# # Python puede evaluar la expresión lógica directamente,
# # respetando el orden de las operaciones.
# resultado_logico = ((3 + 5 * 8) < 3 and (-6 / 3 * 4 + 2 < 2)) or (a > b)
#
# # Mostramos el resultado final
# print(f"\nLa expresión a evaluar es: ((3 + 5 * 8) < 3 and (-6 / 3 * 4 + 2 < 2)) or (a > b)")
# print(f"Con a = {a} y b = {b}")
# print(f"El resultado lógico es: {resultado_logico}")

# Ejercicio 3: Intercambiar el valor de dos variables

# Asignamos los valores iniciales del ejemplo
# a = 10
# b = 5
#
# print(f"--- Valores Iniciales ---")
# print(f"El valor de a es: {a}")
# print(f"El valor de b es: {b}")
#
# # La magia de Python: intercambio en una sola línea
# a, b = b, a
#
# print(f"\n--- Valores Intercambiados ---")
# print(f"El nuevo valor de a es: {a}")
# print(f"El nuevo valor de b es: {b}")

# Ejercicio 4: Área y longitud de un círculo

# En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi
# Se escribe:
# import math
#
# # Hacemos un programa para ingresar el radio de un circulo
# # Usamos float() para que el radio pueda tener decimales (ej: 3.5)
# radio = float(input("Introduce el radio del círculo: "))
#
# # Calculamos el área usando la fórmula: Pi * r^2
# # El valor de Pi lo obtenemos de math.pi
# # La potencia se escribe como ** 2
# area = math.pi * (radio ** 2)
#
# # Calculamos la longitud de la circunferencia: 2 * Pi * r
# longitud = 2 * math.pi * radio
#
# # ...y se reporte su área y la longitud de la circunferencia.
# print(f"\n--- Resultados para el círculo de radio {radio} ---")
#
# # Usamos el formato :.2f dentro del f-string para redondear el resultado a 2 decimales
# print(f"El área del círculo es: {area:.2f}")
# print(f"La longitud de la circunferencia es: {longitud:.2f}")

