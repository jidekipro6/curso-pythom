while True:
    try :
        a=int(input('ingresa un nunero  :'))
        b=int(input('ingrese el numero a multiplicar  :'))
        multiplicacion =a*b
        print('la multiplicacion es ',multiplicacion)
    except TypeError:
        print('debe ingresar un numero')
    except ValueError:
        print('NO INGRESES UNA LETRA PS MRD')
    else:
        print('se a realizado la multiplicacion con exito')
    finally:
        print('OK')
    