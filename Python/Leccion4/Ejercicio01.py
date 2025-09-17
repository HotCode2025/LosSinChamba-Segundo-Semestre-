# Ejercicio 1: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar
# la lista con el bucle for, los elementos deben mostrarse
# de la siguiente forma:
# 1-2-3-4-5...-50

lista = list(range(1, 51))
cadena = ""
for i in lista:
    cadena += str(i) + "-"

print(cadena[:-1]) # El [:-1] elimina el ultimo guion de la cadena