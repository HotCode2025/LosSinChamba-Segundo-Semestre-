class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni #Este atrivuto esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostras_detalle(self): # Self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud', 404040, 40) # Necesitamos enviar argumentos
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto2
# print(persona1.apellido)
# print(persona1.edad)

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 355555,45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}')

persona1.nombre = 'Leandro'
persona1.apellido = 'Orozco'
persona1.edad = 35
persona1.dni = 34870214
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostras_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostras_detalle()

#Persona.mostras_detalle() # Debemos pasarle una referencia para el self o dara error
persona1.telefono ='45454554'
print(f'Este es el Celular de : {persona1.nombre} {persona1.telefono}') # Hemos creado un atributo de un objeto

#print(persona2.telefono) el obj de la persona2 no tiene este atributo, da error
persosa3 = Persona('Luciano', 'Perez','34800800','30' 'Telefono', '29750505050', 'Calle Altm. Zar', 1010, 'Barrio 330', 60, Altura=1.72, Peso=75, CFavorito='Verde', Auto='Fiat Cronos', Modelo=2020)
persosa3.mostras_detalle()
persosa4 = Persona('Agustina', 'Gonzales','2020200' '30','Telefono', '2604606065', 'Av.Mitre', 210, 'Ciudad', Altura=1.58, Peso=50, CFavorito='Azul', Auto='VW Golf', Modelo=2022)
persosa4.mostras_detalle()
# print(persosa4.dni)# esto no se debe utilizar en python, esto dice que desconocemos python (esta encapsulado)
#persona4.__nombre # esta totalmente encapsulado
