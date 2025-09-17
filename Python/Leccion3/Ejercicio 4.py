# --- Calculadora de promedio y calificación más baja (estilo diagrama de flujo) ---

# 1. Definir e inicializar las variables como en el diagrama.
suma = 0.0
# Se inicializa la calificación baja con un número muy alto (o infinito).
# Así, la primera calificación que se ingrese siempre será menor y la reemplazará.
calificacion_baja = float('inf')
total_alumnos = 10

print(f"A continuación, ingrese las calificaciones de los {total_alumnos} alumnos.")
print("-" * 50)

# 2. Iniciar el bucle 'Para' que se repite 10 veces.
for i in range(1, total_alumnos + 1):

    # Bucle interno para asegurar que el usuario ingrese una calificación válida.
    while True:
        try:
            # 3. Pedir que se digite una calificación.
            entrada_str = input(f"Ingrese la calificación del alumno {i}: ")
            # Convertimos a float para aceptar decimales (Como Real en PSeInt).
            calificacion = float(entrada_str)

            # Opcional pero recomendado: validar que la nota esté en un rango lógico.
            if 0 <= calificacion <= 10:
                break  # Si la nota es válida, salimos del bucle de validación.
            else:
                print("Error: La calificación debe estar entre 0 y 10. Intente de nuevo.")

        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número.")

    # 4. Sumar la calificación al total (suma <- suma + calificacion).
    suma += calificacion

    # 5. Comprobar si la calificación actual es la más baja.
    # (calificacion < calificacion_baja)
    if calificacion < calificacion_baja:
        # Si es verdadero, se actualiza el valor de la calificación más baja.
        calificacion_baja = calificacion

# --- Cálculos Finales ---
# 6. Calcular el promedio una vez terminado el bucle.
# (calificacion_promedio <- suma / 10)
calificacion_promedio = suma / total_alumnos

# 7. Imprimir los resultados.
print("-" * 50)
print("\n--- Resultados Finales del Grupo ---")
# Usamos :.2f para mostrar el promedio con solo 2 decimales.
print(f"La calificación promedio es: {calificacion_promedio:.2f}")
print(f"La calificación más baja es: {calificacion_baja}")
