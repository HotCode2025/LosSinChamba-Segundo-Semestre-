# Ejercicio de Colecciones 2

# Listas de jugadores de Boca e Independiente
# Nota: Incluí a "Romero" en ambas listas para ejemplificar un jugador en común.
jugadores_boca = ['Palermo', 'Riquelme', 'Tevez', 'Battaglia', 'Benedetto', 'Romero']
jugadores_independiente = ['Bochini', 'Agüero', 'Milito', 'Mancuello', 'Velasco', 'Romero']

print(f"Lista de jugadores de Boca: {jugadores_boca}")
print(f"Lista de jugadores de Independiente: {jugadores_independiente}")
print("---")

set_boca = set(jugadores_boca)
set_independiente = set(jugadores_independiente)

todos_los_jugadores = set_boca | set_independiente
lista_todos = list(todos_los_jugadores)
lista_todos.sort()

print(f"1. Jugadores que aparecen en las listas (sin repetición):")
print(lista_todos)
print("---")

solo_boca = set_boca - set_independiente
lista_solo_boca = list(solo_boca)
lista_solo_boca.sort()

print(f"2. Jugadores que solo están en Boca:")
print(lista_solo_boca)
print("---")

solo_independiente = set_independiente - set_boca
lista_solo_independiente = list(solo_independiente)
lista_solo_independiente.sort()

print(f"3. Jugadores que solo están en Independiente:")
print(lista_solo_independiente)
print("---")

jugadores_en_ambos = set_boca & set_independiente
lista_en_ambos = list(jugadores_en_ambos)
lista_en_ambos.sort()

print(f"4. Jugadores que aparecen en ambas listas:")
print(lista_en_ambos)
print("---")
