class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):  # Metodo Getter para apellido
        print('Estamos utilizando el método get para apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter para apellido
        print('Estamos utilizando el método set para apellido')
        self._apellido = apellido

    @property
    def edad(self):  # Método Getter para edad
        print('Estamos utilizando el método get para edad')
        return self._edad

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

   # @edad.setter
   # def edad(self, edad):  # Metodo Setter para edad
    #    print('Estamos utilizando el metodo set para edad')
     #   self._edad = edad

if __name__ == '__main__':
     persona1 = Persona2('Ariel', 'Betancud', 40)
     print(persona1.nombre) #Llamamos al metodo getter
     print(persona1.apellido)
     print(persona1.edad)


     persona1.nombre = 'Juan Pedro' # Llamamos el metodo setter
     print(persona1.nombre)
     print(persona1.mostrar_detalles())
     # Atributo read-only seria la edad porque no tiene el metodo set - se ve diferente a su video intente realizarlo solo

     class Persona2:
        # LÍNEA 87 CORREGIDA: '__init__' en lugar de '_init_'
        def __init__(self, altura, peso, alcance):
            self._altura = altura
            self._peso = peso
            self._alcance = alcance

        def mostrar_detalles(self):
            return f'Se muestran los siguientes datos: {self._altura} {self._peso} {self._alcance}'

        @property
        def altura(self): # metodo getter
            print('Usamos metodo get de altura')
            return self._altura

        @altura.setter
        def altura(self, altura): # metodo setter
            print('Usamos metodo set de altura')
            self._altura = altura

        @property
        def peso(self):
            print('Usamos metodo get de peso')
            return self._peso

        @peso.setter
        def peso(self, peso):
            print('Usamos metodo set de peso')
            self._peso = peso

        @property
        def alcance(self):  # metodo getter
            print('Usamos metodo get de alcance')
            return self._alcance

        @alcance.setter
        def alcance(self, alcance):
            print('Usamos metodo set de alcance')
            self._alcance = alcance

     print("\n\n--- PRUEBAS CON LA SEGUNDA CLASE CORREGIDA ---")

     persona1 = Persona2('1.70', '78', '1.92')
     print(f"Altura inicial: {persona1.altura}")
     print(f"Peso inicial: {persona1.peso}")
     print(f"Alcance inicial: {persona1.alcance}")

     print("\n--- Modificando todos los atributos ---")
     persona1.altura = '1.89'
     print(f"Nueva Altura: {persona1.altura}")

     persona1.peso = '85'
     print(f"Nuevo Peso: {persona1.peso}")

     persona1.alcance = '2.05' #
     print(f"Nuevo Alcance: {persona1.alcance}")

     print("\n--- Detalles finales ---")
     print(persona1.mostrar_detalles())

     print(__name__)
