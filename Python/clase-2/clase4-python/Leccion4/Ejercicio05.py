# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
import math # Pedimos al usuario que ingrese un número
numero = int(input("Digite un número positivo: ")) # Verificamos que el número sea positivo
if numero < 0:
    print("El número ingresado es negativo, no se puede calcular el factorial.")
else:
    # Caso especial para el factorial de 0
    if numero == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i

    print(f"El factorial de {numero} es: {factorial}")

#Solucion Profe

numero = int(input("Digite un numero: "))
while numero < 0:  # Mientras el numero sea negativo
    print("Error -> El numero tiene que ser positivo")
    numero = int(input("Digite un número: "))
factorial = 1  # la variable para calcular el factorial
for i in range(1, numero + 1):
    factorial *= i

print(f"\nEl factorial del numero {numero} positivo ingresado es: {factorial}")