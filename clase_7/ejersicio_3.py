#Ejercicio 3: Factorial
# Solicita al usuario un número y calcula el factorial de ese número.
# Nota: El factorial de un número n es el producto de todos los números desde 1 hasta n. Ej: factorial de 5 = 5x4x3x2x1 = 120.
# ========================================

#Ejercico 03
num = int(input ("Ingrese numero: "))

factorial = 1

i = 1
while i <= num:
    factorial *= i
    i += 1

print("El factorial de", num, "es:", factorial)