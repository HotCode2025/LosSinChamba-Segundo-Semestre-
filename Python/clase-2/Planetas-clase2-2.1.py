# CLASE 2 2.1
# tipo set
planetas = {'Tierra', 'Marte', 'Venus', 'Jupiter'}
print(len(planetas)) # Usamos len para ver cuantos elementos tiene = length significa largo 

# Revisar si un elemento existe dentro de set 
print('Tierra' in planetas)  # Devuelve True si existe, False si no
print('Saturno' in planetas)  # Devuelve False

# Agregar un elemento al set
planetas.add('Saturno')
planetas.add('tierra')
print(planetas)  # 'tierra' no se agregará porque los sets son únicos

# Eliminar elementos, puede arrojar un error si el elemento no existe 
planetas.remove("Jupiter") # Esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard("tierra") # Esta funcion no nos presenta ningun error 
print(planetas)

# Limpiar set 
planetas.clear()
print(planetas)

# Eliminar set 
del planetas 
print(planetas) # al eliminar nos muetra fun error 
