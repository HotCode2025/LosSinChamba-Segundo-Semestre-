# --- Calculadora de Salarios de Empleados (traducción del diagrama) ---

# 1. Definir el número de empleados e inicializar la suma total.
#    Corresponde a 'suma <- 0' en el diagrama.
num_empleados = 5
suma_total_salarios = 0.0

print(f"--- Cálculo de salarios para {num_empleados} empleados ---")

# 2. Iniciar el bucle principal que se repite 5 veces (para cada empleado).
#    Corresponde al bucle 'Mientras i <= 5'.
for i in range(1, num_empleados + 1):
    print(f"\n--- Datos del Empleado #{i} ---")

    # Bucle para obtener un número válido de horas.
    while True:
        try:
            horas_trabajadas = float(input("  Digite las horas trabajadas: "))
            if horas_trabajadas >= 0:
                break
            else:
                print("  Error: Las horas no pueden ser un valor negativo.")
        except ValueError:
            print("  Error: Ingrese un número válido para las horas.")

    # Bucle para obtener una tarifa por hora válida.
    while True:
        try:
            tarifa_por_hora = float(input("  Digite la tarifa por hora: $"))
            if tarifa_por_hora >= 0:
                break
            else:
                print("  Error: La tarifa no puede ser un valor negativo.")
        except ValueError:
            print("  Error: Ingrese un número válido para la tarifa.")

    # 3. Calcular el salario del empleado actual.
    #    (salario <- horas * tarifa)
    salario_actual = horas_trabajadas * tarifa_por_hora
    print(f"  => El salario de este empleado es: ${salario_actual:.2f}")

    # 4. Acumular el salario en la suma total.
    #    (suma <- suma + salario)
    suma_total_salarios += salario_actual

# 5. Imprimir el resultado final una vez que el bucle ha terminado.
print("\n" + "=" * 50)
print(f"La suma total de los salarios de todos los empleados es: ${suma_total_salarios:.2f}")
print("=" * 50)
