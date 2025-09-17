# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
# suma de números pares del 2 al 30
# suma = 240

# Definimos el rango de inicio y fin
inicio = 2
fin = 30

# Inicializamos la variable para almacenar la suma
suma = 0

# Iteramos sobre los números del rango
for numero in range(inicio, fin + 1):
    # Verificamos si el número es par usando el operador módulo (%)
    if numero % 2 == 0:
        suma += numero

# Imprimimos el resultado final
print(f"La suma de los números pares del {inicio} al {fin} es: {suma}")


#Solucion Profe
a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))

suma = 0

for i in range(a, b+1):
    if i % 2 == 0: # Esto es si el numero es par
        suma += i

print(f"\nLa suma de números pares dentro del rango es: {suma}")