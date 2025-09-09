names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)
