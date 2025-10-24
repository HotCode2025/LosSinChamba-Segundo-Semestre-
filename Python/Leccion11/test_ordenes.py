from Producto import Producto
from Orden import Orden


producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)

productos1 = [producto1, producto2]  # lista de productos

orden1 = Orden(productos1)
print("--- Orden 1 Creada ---")
print(orden1)

# Creamos la orden2 (que usa la misma lista inicial de productos)
orden2 = Orden(productos1)
print("\n--- Orden 2 Creada (Inicial) ---")
print(orden2)

print("\n=============================================")
print("# Tarea: Modificar la orden2")
print("=============================================")

# 1. Crear los nuevos productos con sus nombres y precios
producto3 = Producto('Zapatos', 350.00)
producto4 = Producto('Corbata', 50.00)
producto5 = Producto('Gorra', 25.50)

# 2. Crear una nueva lista de productos
productos_nuevos_para_orden2 = [producto3, producto4, producto5]

# 3. Agregar la nueva lista de productos a la orden2
#    Iteramos y usamos el metodo agregar_producto()
for producto in productos_nuevos_para_orden2:
    orden2.agregar_producto(producto)

# Opcional: Imprimir la orden2 modificada para verificar el resultado
print("\n--- Orden 2 Modificada (Tarea Realizada) ---")
print(orden2)