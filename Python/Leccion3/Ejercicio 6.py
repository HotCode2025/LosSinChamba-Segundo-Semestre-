# --- Clasificador de números Pares e Impares (traducción del diagrama) ---

# 1. Pedir la cantidad de números a ingresar y validar la entrada.
while True:
    try:
        n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))
        if n_elementos > 0:
            break
        else:
            print("Error: Debe ingresar al menos 1 elemento.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# 2. Inicializar todas las variables en cero, como en el diagrama.
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0

print("-" * 40)
print(f"Ahora, ingrese los {n_elementos} números:")

# 3. Iniciar el bucle principal que se repite 'n_elementos' veces.
for i in range(1, n_elementos + 1):
    # Bucle para validar que cada número ingresado sea un entero.
    while True:
        try:
            num = int(input(f"  Número {i}: "))
            break
        except ValueError:
            print("  Entrada no válida. Intente de nuevo.")

    # 4. Clasificar el número (par o impar) y actualizar contadores/sumas.
    #    Esto corresponde al rombo de decisión 'num MOD 2 = 0'.
    if num % 2 == 0:
        # Rama para números pares (V)
        suma_pares += num
        conteo_pares += 1
    else:
        # Rama para números impares (F)
        suma_impares += num
        conteo_impares += 1

# --- Resultados Finales ---
print("-" * 40)
print("\nAnálisis completado:")

# 5. Mostrar resultados de los números pares, validando si se ingresó alguno.
if conteo_pares == 0:
    print("No se han digitado números pares.")
else:
    print(f"La suma de los números pares es: {suma_pares}")
    print(f"El total de números pares es: {conteo_pares}")

# 6. Calcular y mostrar el promedio de impares, validando para evitar división por cero.
if conteo_impares == 0:
    print("No se han digitado números impares.")
else:
    # Este cálculo solo se hace si hay al menos un número impar.
    promedio_impares = suma_impares / conteo_impares
    # Se formatea el resultado a 2 decimales.

    print(f" El promedio de los números impares es: {promedio_impares:.2f}")
