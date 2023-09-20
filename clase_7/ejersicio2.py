#ejersicio 2
num = int(input("Por favor, ingresa un número: "))
sumpares = 0
for i in range(2, num + 1, 2):
    sumpares += i
print("La suma de los números pares desde 2 hasta", num, "es:", sumpares)
