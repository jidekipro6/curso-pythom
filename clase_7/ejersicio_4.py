# Ejercicio 4: Cadena Reversa
# Pide al usuario una cadena de texto e imprímela en orden inverso.
cad_de_texto = input("Ingrese un texto ")  #el numero ingresado se guarda en :cad_de_texto
texto = len(cad_de_texto) #indicamos que comienze de la ultima letra
indice = texto - 1  #indicamos que el texto ingresado de descuente 1 en 1

cadena_inversa = ""  #inicializamos la variable en vasio
while indice >= 0: # mientras indice sea mayor a 0
    cadena_inversa += cad_de_texto[indice]
    indice -= 1

print("Cadena original:", cad_de_texto)
print("Cadena en orden inverso:", cadena_inversa)