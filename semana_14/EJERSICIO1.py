class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.precio * self.cantidad

# Ejemplo de uso
producto1 = Producto("Camisa", 2.00, 3)
precio_total = producto1.calcular_precio_total()
print(f"El precio total de {producto1.nombre} es: ${precio_total}")