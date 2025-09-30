class Persona2:
    def _init_(self, altura, peso, alcance):
        self._altura = altura
        self._peso = peso
        self._alcance = alcance

    def mostrar_detalles(self):
        print(f'se muestran los siguientes datos: {self._altura} {self._peso} {self._alcance}')

    @property
    def altura(self): #metodo getter
        print('Usamos metodo get')
        return self._altura

    @altura.setter
    def altura(self, altura): #metodo setter
        print('Usamos metodo set')
        self._altura = altura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def alcance(self):  # metodo getter
        return self._alcance

    @alcance.setter
    def alcance(self, alcance):
        self._alcance = alcance


persona1 = Persona2('1.70', '65', '1.74')
print(persona1.altura)
print(persona1.peso)
print(persona1.alcance)

persona1.altura = '1.89'
print(persona1.altura)
persona1.peso = '78'
print(persona1.peso)
persona1.alcance = '1.92'
print(persona1.alcance)


print(persona1.mostrar_detalles())
