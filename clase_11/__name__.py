try:
    num=int(input('ingrese un numero paradividir a 25  :'))
    print(15/num)
except Exception as e:
    print(type(e).__name__)