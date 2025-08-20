# Ejercicio 1: Califica tu día

def calificar_dia():
    """
    Solicita al usuario una calificación para su día (del 1 al 10)
    y muestra un mensaje basado en la calificación.
    """
    while True:
        try:
            # Solicitar la calificación al usuario
            calificacion_str = input("¿Cómo estuvo tu día? Califica del 1 al 10: ")
            calificacion = int(calificacion_str)

            # Validar que la calificación esté en el rango de 1 a 10
            if 1 <= calificacion <= 10:
                print(f"¡Entendido! Tu día estuvo de: {calificacion}.")
                if calificacion >= 8:
                    print("¡Me alegra saber que tuviste un gran día!")
                elif calificacion >= 5:
                    print("Espero que mañana sea aún mejor.")
                else:
                    print("Lamento escuchar eso. ¡Espero que las cosas mejoren pronto!")
                break # Salir del bucle si la calificación es válida
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            # Manejar el error si el usuario no introduce un número
            print("Entrada no válida. Por favor, introduce un número entero.")

# Llamar a la función para ejecutar el programa
if __name__ == "__main__":
    calificar_dia()
