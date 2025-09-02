saldo = 1000

while True:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print(f"Saldo actual: ${saldo}")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == "1":
        cantidad = float(input("¿Cuánto dinero deseas ingresar? $"))
        if cantidad > 0:
            saldo += cantidad
            print(f"Has ingresado ${cantidad}")
            print(f"Tu nuevo saldo es: ${saldo}")
        else:
            print("La cantidad debe ser mayor a 0")
    
    elif opcion == "2":
        cantidad = float(input("¿Cuánto dinero deseas retirar? $"))
        if cantidad > 0:
            if cantidad <= saldo:
                saldo -= cantidad
                print(f"Has retirado ${cantidad}")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:
                print("No tienes suficiente saldo")
        else:
            print("La cantidad debe ser mayor a 0")
    
    elif opcion == "3":
        print(f"Tu saldo disponible es: ${saldo}")
    
    elif opcion == "4":
        print("Gracias por usar el cajero automático")
        break
    
    else:
        print("Opción no válida. Selecciona del 1 al 4")