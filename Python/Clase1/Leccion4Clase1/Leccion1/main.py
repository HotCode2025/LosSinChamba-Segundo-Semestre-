"""
miVariable = 3'
print(miVariable)
miVariable = "Hola a todos"
print (miVariable)
miVariable = 3.5
print(miVariable)
x= 10
y = 2
z = x + y
print(id(x))
print(id(y))
print(id(z))
print(id(miVariable))


a: str = "Hola a todos"
print (type(a))

a= False
print(type(a))

# Tipos int, float, String, Bool
x= 10
print(x)
print (type(x))
x=14.5
print(x)
print(type(x))
x= "Hola Mundo"
print(x)
print(type(x))
x=True
print(x)

# Manejo de Cadenas(String)

miGrupoFavorito = "Red Hod Chilli Papper:"
caracterisricas = "Banda de Rock "

print("Mi grupo favorito es:", miGrupoFavorito ,caracterisricas)

numero1 = "7"
numero2 = "8"
print (int(numero1) + int(numero2))

# Tipos Boleanos (bool)
miBooleano = True
print(miBooleano)
miBooleano = 3 > 2
print(miBooleano)


if miBooleano:
    print("El resultado es Verdadero")
else:
    print("El resultado es Falso")

# Procesar la entrada del usuario
# Funcion inpud

#resultado = input("Digite un numero: ")  # regresar un dato tipo string
#print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer nuemro:"))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
"""
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("Resultado de la suma",suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicaion = operandoA * operandoB
print(f'El rasultado de la multiplicacion es:{multiplicaion}')

division = operandoA / operandoB
print(f'El resultado de la division es:{division}')
division = operandoA // operandoB
print(f'El resultado de la division (int) es: {division}')
modulo = operandoA % operandoB
print(f'El resultado de la division o residuo (modulo) es: {modulo}')
exponente = operandoA ** operandoB
print(f"El resultado del exponente es:{exponente}")
"""
'''
alto = int (input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area:', area )
print('Perimetro:',perimetro )
'''
"""
miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion

miVariable3 = miVariable3+ 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparacion

d= 4
b = 2
resultado = d == b # comprobamos si son iguales
print(resultado)
#Operadores diferentes
resultado = d != b
print(resultado)
# operador Mayor que
resultado = d > b
print(resultado)
#Operador Menor o igual que
resultado = b <= b
print(resultado)
#Operador mayor o igual que
resultado = b >= b
print(resultado)
"""
'''
a = int(input("Digite un numero:") )
print(f"El residuo de la division es :{a % 2}")
if a % 2 == 0:
    print(f"El valor de a es:{a} es un numero Par")
else:
    print(f"El valor de a es:{a} es un numero IMPAR ")
'''
"""
edadAdulto = 18
edadPersona = int(input("Digite su edad:"))
if edadPersona >= edadAdulto:
    print(f'Su edad es: {edadPersona} años, usted es mayor de edad')
else:
    print(f'Su edad es :{edadPersona} años, usted es menor de edad')
"""
"""
# Operadores Logicos
a = False
B = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""
'''
# Ejercicio Valor dentro de un rango

valor = int(input("Digite un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and  valor <= valorMaximo
if dentroRango:
    print(f'El valor {valor} No esta dentro del rango')
else:
    print(f'El valor {valor} No esta dentro del rango')
'''
'''
# Ejercicio con el operador or, Operador not
vacaciones = False
diaDescanso = True

if not (vacaciones or diaDescanso):
    print('Tiene Trabajo que hacer')

else:
    print('Puede asistir al juego')
'''
'''
#Ejercicio: Rango entre 20 y 30 años
edad = int(input("Digite su edad:"))
veinte = edad >= 20 and edad < 30
print(veinte)

treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print('Estas dentro del rango de lo (20\'0) años')
    elif treinta:
        print('Estas dentro del rango de los (30\'0) años')40
    else:
        print("No esta dentro del rango")
else:
        print("No esta dentro del rango de los (20'0) a (30'0) años")

'''
'''
#Ejercicios : El mayo de dos numero
numero1 = int(input('Digite el valor para el numero1:'))
numero2 = int(input('Digite el valor para el numero2:'))

if numero1 > numero2:
    print('El numero 1 es mayor')
else:
    print('El numero 2 es mayo')
'''

# Ejercicio: Tienda de libros
print('Digite los siguientes datos del libro')
nombre = input('Digite el nombre del Libro: ')
id = int(input('Digite el ID del Libro: '))
precio = float(input('Digite el precio del Libro: '))
envioGratuito = input('Indicar si el envio es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
      ''')

