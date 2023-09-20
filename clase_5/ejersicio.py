print("\n\n\n<-------------------------------------------------------------->\n\n\n")
# 1. Edad para Votar
# Dado una edad, determina si la persona puede votar. En este país, se puede votar a partir de los 18 años.
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print ("puede votar")
else:
    print ("no puede votar")


print("\n\n\n<-------------------------------------------------------------->\n\n\n")

print("\n\n\n<-------------------------------------------------------------->\n\n\n")
# 2. Comparación de Números
# Dados dos números, indica cuál es el mayor o si son iguales.
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))


if a > b:
    print("a es mayor")
elif b>a:
    print("b es mayor")
else:
    print ("son iguales")


