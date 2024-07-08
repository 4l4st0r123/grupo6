import mysql.connector

class Catalogo:    

    def __init__(self, host: str, user: str, password: str, database: str):
        self.conn = mysql.connector.connect(
            host=host,
            port=3307,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS productos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(4))'''
        )
        self.conn.commit()
        
    # Definimos una lista de diccionarios
    productos = []

    def agregar_producto(self, descripcion: str, cantidad: int, precio: float, 
                        imagen: str, proveedor: int):

        sql = "INSERT INTO productos (descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s)"
        valores = (descripcion, cantidad, precio, imagen, proveedor)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def consultar_producto(self, codigo: int):
        self.cursor.execute(f"SELECT * FROM productos Where codigo = {codigo}")
        return self.cursor.fetchone()


    def modificar_producto(self, codigo: int, nueva_descripcion: str, 
                            nueva_cantidad: int, nuevo_precio: float, 
                            nueva_imagen: str, nuevo_proveedor: int):
        sql = """UPDATE productos SET description = %s, cantidad = %s, 
                precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"""
        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen,
                    nuevo_proveedor, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def mostrar_producto(self, codigo: int):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código     | {producto['codigo']}")
            print(f"Descripción| {producto['descripcion']}")
            print(f"Cantidad   | {producto['cantidad']}")
            print(f"Precio     | {producto['precio']}")
            print(f"Imagen     | {producto['imagen_url']}")
            print(f"Proveedor: | {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")
        
        print()


    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos
            

    def eliminar_producto(self, codigo: int):
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    


"""
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
"""

catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')
# Agregamos productos a la tabla
catalogo.agregar_producto('Teclado USB 101 teclas', 10, 4500,
                            'teclado.jpg', 101)
catalogo.agregar_producto('Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto('Monitor LED', 5, 25000, 'monitor.jpg', 102)


cod_prod = int(input("Ingrese el código del producto: "))
producto = catalogo.consultar_producto(cod_prod)
if producto:
    print(f"Producto encontrado: {producto['codigo']} - {producto['descripcion']}")
else:
    print(f'Producto {cod_prod} no encontrado.')


catalogo.mostrar_producto(1)
catalogo.modificar_producto(1, 'Teclado mecánico', 20, 34000, 'tecmec.jpg', 106)
catalogo.mostrar_producto(1)


productos = catalogo.listar_productos()
for producto in productos:
    print(producto)


catalogo.eliminar_producto(2)
productos = catalogo.listar_productos()
for producto in productos:
    print(producto)