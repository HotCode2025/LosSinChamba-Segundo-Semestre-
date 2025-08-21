# Ejercicio 2

# Este programa solicita al usuario el título y el autor de un libro,
# luego imprime la información en un formato específico.

def obtener_info_libro():
  """
  Solicita al usuario el título y el autor de un libro y los imprime.
  """
  # Solicita el título del libro al usuario
  print("Proporciona el título:")
  titulo = input() # Lee la entrada del usuario para el título



  # Solicita el autor del libro al usuario
  print("Proporciona el autor:")
  autor = input() # Lee la entrada del usuario para el autor

  # Imprime la información del libro en el formato solicitado
  print(f"{titulo} fue escrito por {autor}")

# Llama a la función para ejecutar el programa
if __name__ == "__main__":
  obtener_info_libro()
