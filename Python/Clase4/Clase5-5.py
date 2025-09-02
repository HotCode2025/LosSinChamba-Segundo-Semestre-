# Ejercicio 6

# Pedimos un numero entero
numero = int(input("Ingrese un número: "))


tabla = []

# Recorremos la tabla, hasta multiplicar el numero por 10
for i in range(1, 11):
    tabla.append(numero * i)

print(f"La tabla de multiplicar de {numero} es: {tabla}")

#Los Sin Chamba