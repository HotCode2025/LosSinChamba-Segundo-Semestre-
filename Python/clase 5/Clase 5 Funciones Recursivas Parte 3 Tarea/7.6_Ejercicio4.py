# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

def calcular_pago_con_impuesto(pago_sin_impuesto, porcentaje_impuesto):
    """
    Calcula el total de un pago incluyendo el impuesto (IVA).
    Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    """
    return pago_sin_impuesto + pago_sin_impuesto * (porcentaje_impuesto / 100)

# Ejemplo de uso
if __name__ == "__main__":
    print("=== CALCULADORA DE IMPUESTOS (IVA) ===")
    
    # Ejemplo del ejercicio
    pago_sin_impuesto = 1000
    porcentaje_impuesto = 21
    
    pago_total = calcular_pago_con_impuesto(pago_sin_impuesto, porcentaje_impuesto)
    
    print(f"Proporcione el pago sin impuesto: {pago_sin_impuesto}")
    print(f"Proporcione el monto del impuesto: {porcentaje_impuesto}%")
    print(f"Pago con impuesto: ${pago_total:,.2f}")
    
    # Ejemplos adicionales
    print("\nEjemplos adicionales:")
    print(f"$500 + 16% IVA = ${calcular_pago_con_impuesto(500, 16):,.2f}")
    print(f"$1500 + 10.5% IVA = ${calcular_pago_con_impuesto(1500, 10.5):,.2f}")