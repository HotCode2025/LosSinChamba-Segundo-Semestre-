# --- Calculadora de Factorial (traducción del diagrama) ---

# 1. Bucle de validación para asegurar que el número sea >= 0.
#    Corresponde al primer bucle 'Repetir' del diagrama.
while True:
    try:
        num_str = input("Digite un número entero mayor o igual a 0: ")
        num = int(num_str)

        if num >= 0:
            break  # Si el número es válido, salimos del bucle.
        else:
            print("Error: El número no puede ser negativo. Intente de nuevo.")

    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número entero.")

# 2. Inicializar la variable del factorial en 1.
#    Esto es crucial porque 0! = 1 y es el neutro multiplicativo.
factorial = 1

# 3. Calcular el factorial con un bucle 'Mientras' (o 'for' en Python).
#    Este bucle se ejecuta solo si num > 0. Si num es 0, se salta
#    y 'factorial' se queda en 1, lo cual es correcto.
for i in range(1, num + 1):
    # En cada iteración, se multiplica el resultado por el número actual.
    # (factorial <- factorial * i)
    factorial *= i

# 4. Imprimir el resultado final.
print("-" * 30)
print(f"El factorial de {num} (es decir, {num}!) es: {factorial}")