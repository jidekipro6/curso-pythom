lista=[1,2,3]  #modificable
tupla=(1,2,3)  # NO MODIFICABLE
print(lista)
print(tupla)

print(lista[0])
print(tupla[0])
#----------set---------

set1=set([1,2,3,4,5,6,7,8])
set2=set([0,2,23,25,56,67])

print(set1-set2) 
print(set2-set1)
print(set1 & set2)   #interseccion
print(set1 | set2)    #union

#--------diccionario---------

persona={'nombre':'raul','apellido':'quijua','edad':'20','sexo':'Masculino'}

print('apellido' in persona)