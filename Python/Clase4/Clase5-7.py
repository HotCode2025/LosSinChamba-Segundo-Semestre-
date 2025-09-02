# Ejercicio 8

saldo = 1000  # saldo inicial

# Definimos nuestro menu interactivo
while True:
    print("\nMenú Cajero Automático ")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = input("Elija una opción (1-4): ") # Permitimos al usuario elegir una de las opciones

    if opcion == "1":
        ingreso = float(input("Ingrese el monto a depositar: "))
        saldo += ingreso
        print(f"Se ingresaron {ingreso}$. Saldo actual: {saldo}$")

    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Se retiraron {retiro}$. Saldo actual: {saldo}$")

    elif opcion == "3":
        print(f"Dinero disponible: {saldo}$")

    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

#Los Sin Chamba