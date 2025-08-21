# Bucle principal que se ejecuta indefinidamente hasta que el usuario decida salir.
# Esto implementa la estructura repetitiva del diagrama de flujo.
while True:
    try:
        # Pedimos al usuario que ingrese el año, como en el diagrama.
        anio_str = input("Ingrese un año para verificar: ")

        # Intentamos convertir la entrada a un número entero.
        anio = int(anio_str)

        # Esta es la condición clave del diagrama de flujo para saber si un año es bisiesto.
        # Regla: Un año es bisiesto si es divisible por 4,
        # excepto si es divisible por 100, a menos que también sea divisible por 400.
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"El año {anio} ES bisiesto.")
        else:
            print(f"El año {anio} NO es bisiesto.")

    except ValueError:
        # Si el usuario no ingresa un número, se muestra un error.
        print("Error: Por favor, ingrese un número de año válido.")

    print("-" * 30)  # Un separador para mayor claridad

    # Preguntamos al usuario si desea continuar, como en la parte final del diagrama.
    opcion = input("¿Desea verificar otro año? (Digite 's' para sí / cualquier otra tecla para salir): ")

    # Si la respuesta no es 's' (o 'S'), se rompe el bucle y termina el programa.
    if opcion.lower() != 's':
        break

# Mensaje de despedida al finalizar el proceso.
print("\nPrograma finalizado. ¡Hasta luego!")