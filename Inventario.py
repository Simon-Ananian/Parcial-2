from Producto import ProductoNoPerecedero, ProductoPerecedero

class Inventario:
    def __init__(self):
        self.productos = []


    def start(self):
        while True:
            print("\nBienvenido al manejo del inventario de productos! \nPor favor elija una de las siguientes opciones")
            print("\n1. Agregar producto al inventario. \n2. Eliminar un producto del inventario. \n3. Buscar un producto por nombre. \n4. Listar todos los productos disponibles.")
            menu = input("---> ")

            if menu == '1':
                self.agregar_producto()
            elif menu == '2':
                self.eliminar_produto()
            elif menu == '3':
                self.buscar_producto()
            elif menu == '4':
                self.listar_productos()

    def agregar_producto(self):
        while True:
            nombre = input("Por favor ingrese el nombre del producto: ").lower()
            precio = float(input("Por favor elija que precio va a tener: "))
            if precio <= 0:
                print("Ha ingresado un dato invalido por favor intentelo de nuevo")
                break
            cantidad = int(input("Por favor indique cuantas unidades de este producto tendrá en su inventario: "))
            if cantidad < 0:
                print("Ha ingresado un dato invalido, por favor intentelo de nuevo.")
                break
            perece = input("Por favor elija que caracteristica desea que tena su producto \n1. Perecedero \n2. No Perecedero \n--->")
            if perece == '1':
                expiracion = str(input("Por favor ingrese una fecha de expiración. Hagalo en este formato (dd/mm): "))
                producto = ProductoPerecedero(nombre, precio, cantidad, expiracion)
                self.productos.append(producto)
                print("Producto añadido al inventario!")
                return self.productos

            if perece == '2':
                material = input("Ingrese el material del que esta hecho su producto: ")
                producto = ProductoNoPerecedero(nombre, precio, cantidad, material)
                self.productos.append(producto)
                print("Producto añadido al inventario!")
                return self.productos
            else:
                print("Ha ingresado un dato invalido, por favor intentelo de nuevo.")

    def eliminar_produto(self):
        pass

    def buscar_producto(self):
        print("---- Menú de Busqueda de Productos ----")
        busqueda = input("\nPor favor ingrese el nombre del producto que desea buscar: ").lower()
        for producto in self.productos:
            if busqueda == producto.nombre:
                print(f"{producto.nombre}, cantidad: {producto.cantidad}, precio: {producto.precio}")


    def listar_productos(self):
        idx = 1
        print("---- Inventario de Productos ----")
        print("Productos disponibles en la tienda: ")
        while idx <= len(self.productos):
            for producto in self.productos:
                print(f"{idx}. {producto.nombre}, cantidad: {producto.cantidad}, precio: {producto.precio}")
                idx += 1
                if producto.cantidad == 0:
                    print("Se le ha agotado este producto!")