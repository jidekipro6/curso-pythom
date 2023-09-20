a=int(input('INGRESA UN NUMERO :'))
b=int(input("ingrese otro numero: "))
operacion =str(input('  el tipo de operacion  suma =+  resta = -  multiplicacion=* divicion =/   :'))
if operacion == '+'or operacion=='suma'or operacion=='sumar':
    suma=a+b
    print(suma)
elif operacion=='-'or operacion=='resta':
    resta=a-b
    print(resta)
elif operacion=='*'or operacion=='multiplicacion':
    multiplicacion=a*b
    print(multiplicacion)
elif operacion=='/'or operacion=='divicion':
    div=a/b
    print(div)
