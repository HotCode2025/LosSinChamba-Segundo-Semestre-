numero = int(input("Ingresa un número positivo: "))

if numero < 0:
    print("Por favor ingresa un número positivo")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    
    print("El factorial de", numero, "es:", factorial)