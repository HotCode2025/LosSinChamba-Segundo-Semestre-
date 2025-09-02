# Ejercicio 3: Insertar elementos y ordenarlos

lista = []
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    else:
        lista.append(numero)
lista.sort()

print("Los números ordenados de menor a mayor son:", lista)