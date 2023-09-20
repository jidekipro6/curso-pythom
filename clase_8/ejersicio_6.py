# Respuesta Ejercicio 3: Actualización de Precios
productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.7,
    "uvas": 2.5,
    "leche": 1.2
}

producto = input("Ingrese el nombre del producto: ")
if producto in productos:
    nuevo_precio = float(input(f"Ingrese el nuevo precio para {producto}: "))
    productos[producto] = nuevo_precio
    print(f"El precio de {producto} ha sido actualizado a {nuevo_precio}")
else:
    print(f"{producto} no está en la lista de productos.")