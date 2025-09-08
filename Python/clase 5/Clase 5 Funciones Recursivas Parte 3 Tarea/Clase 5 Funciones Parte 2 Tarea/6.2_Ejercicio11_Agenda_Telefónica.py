# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

def main():
    agenda = {}
    
    while True:
        print("\n1. Nuevo contacto")
        print("2. Borrar contacto")
        print("3. Ver contactos existentes")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono
            print("Contacto agregado.")
        
        elif opcion == "2":
            nombre = input("Nombre a borrar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        
        elif opcion == "3":
            if agenda:
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos.")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()