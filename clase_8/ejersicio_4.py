# ========================================
# Ejercicio 2: Conjuntos y Repetición
# Solicita al usuario que ingrese números enteros uno por uno. 
# Almacena estos números en un conjunto para garantizar que no haya repetidos.
# Cuando el usuario ingrese el número -1, finaliza la entrada y muestra el conjunto final de números ingresados.
# ========================================

numero={}
masnumeros='si'

while masnumeros=='si':
    numeroagregado=int(input("INGRESE UN NUMERO ENTERO :"))
    numero[numeroagregado]=numero
    
    if numeroagregado==-1:
        masnumeros='no'
    else:
        masnumeros=input("ingresaras mas numero si o no :")
print(f"estos son los numeros que ingreso:",numero)
