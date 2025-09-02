import random

# Ejercicio 7

# Definimos las variables
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

# Mostramos un mensaje de bienvenida
print("Bienvenido al juego: Adivina el número (entre 1 y 100)")

# Usamos el ciclo WHILE para contar la cantidad de intentos
while not adivinado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número secreto es mayor")
    elif intento > numero_secreto:
        print("El número secreto es menor")
    else:
        adivinado = True
        print(f"¡Felicitaciones! Adivinaste el número {numero_secreto} en {intentos} intentos.")

#Los Sin Chamba