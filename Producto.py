class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def __str__(self):
        return f"nombre: {self.nombre}, cantidad: {self.cantidad}, precio: {self.precio}, fecha de expiracion: {self.fecha_expiracion}"

class ProductoNoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, material):
        super().__init__(nombre, precio, cantidad)
        self.material = material

    def __str__(self):
        return f"nombre: {self.nombre}, cantidad: {self.cantidad}, precio: {self.precio}, material: {self.material}"