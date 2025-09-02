# Ejercicio 1: Llenar una lista con los números del 1 al 50
# y mostrarla con el formato: 1-2-3-...-50

print("Opción 1:")
numeros = list(range(1, 51))

for i in range(len(numeros)):
    print(numeros[i], end='')
    if i < len(numeros) - 1:
        print('-', end='')

print("\n" + "=" * 20)
print("Opción 2:")
for numero in range(1, 51):
    print(numero, end='')
    if numero < 50:
        print('-', end='')