# --- Contador de números positivos, negativos y neutros ---

# 1. Definir e inicializar los contadores en cero, como en el diagrama.
conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0

print("A continuación, ingrese 10 números enteros.")
print("-" * 30)

# 2. Crear un bucle 'Para' que se repita 10 veces (de 1 a 10).
# Esto corresponde al bloque morado del diagrama.
for i in range(1, 11):

    # Usamos un bucle interno para validar la entrada.
    # Si el usuario no escribe un número, se lo pedirá de nuevo.
    while True:
        try:
            # 3. Pedir al usuario que digite un número.
            entrada_str = input(f"Ingrese el número {i} de 10: ")
            num = int(entrada_str)
            break  # Si la conversión a entero funciona, salimos del bucle de validación.
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero.")

    # 4. Clasificar el número usando una estructura if/elif/else.
    # Esto representa la serie de rombos (decisiones) del diagrama.
    if num > 0:
        # Si num > 0 es verdadero, incrementa el contador de positivos.
        conteo_positivos += 1
    elif num < 0:
        # Si num > 0 es falso, se revisa si num < 0.
        # En el diagrama, esto corresponde al "F" (falso) de la primera decisión.
        conteo_negativos += 1
    else:
        # Si no es mayor ni menor que cero, es un cero (neutro).
        conteo_neutros += 1

# 5. Al terminar el bucle, imprimir los resultados finales.
print("-" * 30)
print("\n--- Resultados del Conteo ---")
print(f" Cantidad de números positivos: {conteo_positivos}")
print(f" Cantidad de números negativos: {conteo_negativos}")
print(f"Cantidad de números neutros (cero): {conteo_neutros}")