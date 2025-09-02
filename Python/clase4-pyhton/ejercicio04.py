inicio = int(input("Ingresa el número de inicio del rango: "))
fin = int(input("Ingresa el número de fin del rango: "))

suma = 0

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma += numero

print(f"La suma de números pares del {inicio} al {fin} es: {suma}")