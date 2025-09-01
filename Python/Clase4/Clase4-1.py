# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos una lista con jugadores históricos de Independiente, incluyendo algunos repetidos
jugadores_independiente = [
'Ricardo Bochini','Sergio Agüero','Gabriel Milito','Jorge Burruchaga','Ricardo Bochini','Arsenio Erico','Sergio Agüero','Ricardo Pavoni','Diego Forlán','Gabriel Milito']

print("--- Lista Original con Jugadores Repetidos ---")
print(jugadores_independiente)
print(f"Total de jugadores en la lista original: {len(jugadores_independiente)}")

jugadores_sin_repetir = []

for jugador in jugadores_independiente:

    if jugador not in jugadores_sin_repetir:
        # Si no está, lo agregamos
        jugadores_sin_repetir.append(jugador)

print("\n--- Lista Final Sin Jugadores Repetidos ---")
print(jugadores_sin_repetir)
print(f"Total de jugadores en la lista final: {len(jugadores_sin_repetir)}")
