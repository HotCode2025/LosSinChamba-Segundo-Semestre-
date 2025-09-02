# Ejercicio 5

#Pedimos el numero entero positivo
numero = int(input("Ingrese un número positivo: "))

# Aclaramos que el numero ingresado debe ser positivo
if numero < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")

# Los sin Chamba