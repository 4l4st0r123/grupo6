import mysql.connector

class Catalogo:
    # Definimos una lista de diccionarios
    productos = []

    def agregar_producto(self, codigo: int, descripcion: str, cantidad: int,
                         precio: float, imagen: str, proveedor: int):
        if self.consultar_producto(codigo):
            return False

        nuevo_producto = {
            'codigo': codigo, 'descripcion': descripcion,
            'cantidad': cantidad, 'precio': precio,
            'imagen': imagen, 'proveedor': proveedor
        }
        self.productos.append(nuevo_producto)
        return True

    def consultar_producto(self, codigo: int):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
            
        return False

    def modificar_producto(self, codigo: int, nueva_descripcion: str, nueva_cantidad: int,
                           nuevo_precio: float, nueva_imagen: str, nuevo_proveedor: int):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False

    def listar_productos(self):
        print("-" * 50)
        for producto in self.productos:
            print(f"Código     | {producto['codigo']}")
            print(f"Descripción| {producto['descripcion']}")
            print(f"Cantidad   | {producto['cantidad']}")
            print(f"Precio     | {producto['precio']}")
            print(f"Imagen     | {producto['imagen']}")
            print(f"Proveedor: | {producto['proveedor']}")
            print("-" * 50)
            
        print()

    def eliminar_producto(self, codigo: int):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
            
        return False

    def mostrar_producto(self, codigo: int):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 50)
            print(f"Código     | {producto['codigo']}")
            print(f"Descripción| {producto['descripcion']}")
            print(f"Cantidad   | {producto['cantidad']}")
            print(f"Precio     | {producto['precio']}")
            print(f"Imagen     | {producto['imagen']}")
            print(f"Proveedor: | {producto['proveedor']}")
            print("-" * 50 + "\n")
        else:
            print("Producto no encontrado.")
        
catalogo = Catalogo()
catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 
                          'teclado.jpg', 101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 
                          'monitor22.jpg', 103)
catalogo.agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 
                          'monitor27.jpg', 104)
catalogo.agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)
catalogo.agregar_producto(3, 'Parlantes USB', 4, 2500, 'parlantes.jpg', 105)

print()
print("Listado de productos:")
catalogo.listar_productos()
print()
print("Datos de un producto:")
catalogo.mostrar_producto(1)
catalogo.eliminar_producto(1)
print()
print("Listado de productos:")
catalogo.listar_productos()
