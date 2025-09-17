# --- Calcular la suma de los primeros N números (usando la fórmula de Gauss) ---

try:
    n_str = input('Digite la cantidad de números a sumar (N): ')
    n = int(n_str)

    if n < 0:
        print("Error: Por favor, ingrese un número entero positivo.")
    else:
        # Aplicamos la fórmula directamente
        suma_total = n * (n + 1) // 2

        print(f"Usando la fórmula matemática, la suma de los primeros {n} números es: {suma_total}")

except ValueError:
    print("Error: La entrada no es un número válido.")
# Opcion 2

# --- Calcular la suma de los primeros N números (usando un bucle) ---

try:
    # 1. Pedir el número N al usuario, como en el diagrama.
    n_str = input('Digite la cantidad de números a sumar (N): ')

    # 2. Convertir la entrada a un número entero.
    n = int(n_str)

    # Validamos que N sea un número positivo para que el cálculo tenga sentido.
    if n < 0:
        print("Error: Por favor, ingrese un número entero positivo.")
    else:
        # 3. Inicializar la variable para la suma, como 'suma <- 0'.
        suma_total = 0

        # 4. Crear el bucle 'Para' (for) que va desde 1 hasta N.
        # En Python, range(1, n + 1) genera números desde 1 hasta n (inclusive).
        for i in range(1, n + 1):
            # 5. Acumular la suma en cada iteración: suma <- suma + i
            suma_total += i

        # 6. Mostrar el resultado final, como en el último paso del diagrama.
        print(f"La suma de los primeros {n} números es: {suma_total}")

except ValueError:
    # Si el usuario no ingresa un número, se muestra un error.

    print("Error: La entrada no es un número válido.")
