class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    # Pruebas básicas (no es la tarea principal, solo verifica la clase Producto)
    producto_test1 = Producto('Zumo', 2.50)
    producto_test2 = Producto('Pan', 1.00)
    print("--- Pruebas de Producto ---")
    print(producto_test1)
    print(producto_test2)
    print(f"Total de productos creados: {Producto.contador_productos}")