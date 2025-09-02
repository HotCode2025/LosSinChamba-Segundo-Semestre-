import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Juego de adivinar el número!")
print("He pensado un número entre 1 y 100")
print("Intenta adivinarlo")

while True:
    numero = int(input("Ingresa un número: "))
    intentos += 1
    
    if numero > numero_secreto:
        print("Es menor")
    elif numero < numero_secreto:
        print("Es mayor")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto}")
        print(f"Lo lograste en {intentos} intentos")
        break
