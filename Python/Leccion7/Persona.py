'''class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):  # Esta clase es hija de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

emplado1 = Empleado('Ariel', 40, 75000)
print(emplado1.nombre)
print(emplado1.edad)
print(emplado1.sueldo)'''

# Tarea: encapsular los atributos y agregar los métodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

class Persona:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Getter para edad
    def get_edad(self):
        return self._edad

    # Setter para edad
    def set_edad(self, edad):
        self._edad = edad


    def __str__(self):
        return f'Persona [Nombre: {self._nombre}, Edad: {self._edad}]'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        # Atributo encapsulado
        self._sueldo = sueldo

    # Getter para sueldo
    def get_sueldo(self):
        return self._sueldo

    # Setter para sueldo
    def set_sueldo(self, sueldo):
        self._sueldo = sueldo


    def __str__(self):
        return f'Empleado [Sueldo: {self._sueldo}] {super().__str__} '


# --- Código Original ---
emplado1 = Empleado('Ariel', 40, 75000)
print('--- Datos de Empleado 1 (Original) ---')
# Acceso a través de los métodos getters
print(f'Nombre: {emplado1.get_nombre()}')
print(f'Edad: {emplado1.get_edad()}')
print(f'Sueldo: {emplado1.get_sueldo()}')
print(emplado1)
print('-' * 40)

# 1. Crear otro objeto y pasar los datos

empleado2 = Empleado('Brenda', 28, 55000)
print('--- Datos de Empleado 2 (Original) ---')
print(f'Nombre: {empleado2.get_nombre()}')
print(f'Edad: {empleado2.get_edad()}')
print(f'Sueldo: {empleado2.get_sueldo()}')
print(empleado2)
print('-' * 40)

# 2. Modificar los datos usando los métodos setters

print('--- Modificando datos de Empleado 2 ---')
empleado2.set_nombre('Brenda Sofía')
empleado2.set_edad(29)
empleado2.set_sueldo(60000)
print('¡Datos modificados! Nombre, edad y sueldo actualizados.')
print('-' * 40)

# 3. Mostrar nuevamente los datos

print('--- Datos de Empleado 2 (Modificado) ---')
print(f'Nuevo Nombre: {empleado2.get_nombre()}')
print(f'Nueva Edad: {empleado2.get_edad()}')
print(f'Nuevo Sueldo: {empleado2.get_sueldo()}')
print(empleado2)
print('-' * 40)
