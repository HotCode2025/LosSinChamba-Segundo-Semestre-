# Ejercicio 2: Modificar los elementos de una lista

# Llenar una lista con los números del 1 al 10
lista_numeros = list(range(1, 11))

try:
    valor_multiplicador = int(input("Ingresa un número para multiplicar la lista: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
    exit()
for i in range(len(lista_numeros)):
    lista_numeros[i] = lista_numeros[i] * valor_multiplicador
print("La lista original era:", list(range(1, 11)))
print("La lista modificada es:", lista_numeros)