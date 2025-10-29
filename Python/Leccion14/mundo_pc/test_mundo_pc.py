from mundo_pc.computadora import Computadora # Corregido: solo importa la clase Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

# --- 1. Crear las instancias iniciales (monitor1 y computadora1) ---
# Se necesitan estas instancias porque las usas más adelante en el código.

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '15 Pulgadas')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


# --- 2. Crear las demás instancias ---

teclado2 = Teclado('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', '27 Pulgadas')
raton2 = Raton('Acer', 'Bluetooth')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

teclado3 = Teclado('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', '32 Pulgadas')
raton3 = Raton('Gamer', 'Bluetooth')
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)


teclado4 = Teclado('Apple', 'Bluetooth')
monitor4 = Monitor('Apple', '27 Pulgadas')
raton4 = Raton('Apple', 'Bluetooth')
computadora4 = Computadora('Apple', monitor4, teclado4, raton4)

teclado5 = Teclado('Samsung', 'Bluetooth')
monitor5 = Monitor('Samsung', '27 Pulgadas')
raton5 = Raton('Samsung', 'Bluetooth')
computadora5 = Computadora('Samsung', monitor5, teclado5, raton5)

# Aquí utilizas instancias que ya están creadas (monitor1, teclado2, raton4, etc.)
computadora6 = Computadora('Samsung', monitor1, teclado2, raton4)
computadora7 = Computadora('Gamer', monitor2, teclado3, raton5)

# --- 3. Crear y procesar las Órdenes ---

computadoras1 = [computadora1, computadora2, computadora7, computadora4]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora3, computadora5, computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora1)
print(orden2)