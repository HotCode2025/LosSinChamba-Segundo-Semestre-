# Ejercicio 4

# Pedimos numero inicial y numero final del rango
inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))

suma = 0

# Recorremos el rango
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:   # Verificamos si es par
        suma += numero

print(f"La suma de los números pares entre {inicio} y {fin} es: {suma}")

# Los Sin Chamba
