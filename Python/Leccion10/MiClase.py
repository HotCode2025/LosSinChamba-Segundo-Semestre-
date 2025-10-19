class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): # La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_statistico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_metodo(self):
        self.metodo_clase()
        self.metodo_statistico()
        print(self.variable_clase)
        print(self.variable_instancia)


print(MiClase.variable_clase)
miClase1 = MiClase('esta es una variable de instancia')
print(miClase1.variable_instancia)
print(MiClase.variable_clase)
miClase2 = MiClase('esta es otra una variable de clase')
print(miClase2.variable_instancia)
print(MiClase.variable_clase)


MiClase.variable_clase2 = 'Valor de variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

MiClase.metodo_statistico()

MiClase.metodo_clase()
miObjeto1 = MiClase('esta es una variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_statistico()