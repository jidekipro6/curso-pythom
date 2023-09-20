#Ejercicio 6: Múltiplos de Tres
# Solicita un número N al usuario e imprime todos los múltiplos de 3 desde 3 hasta N.

n = int(input("Ingresa un número: "))

print("Múltiplos de 3 desde 3 hasta", n, ":")

for i in range(3, n + 1, 3):
    print(i)