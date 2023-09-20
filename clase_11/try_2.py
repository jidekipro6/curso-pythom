try:
    num=int(input('ingrese un nuero para dividir entre 100  :'))
    if num==0:
        raise ValueError('q no puedes dividir por 0')
    print(100/num)
except Exception as e:
    print(e)