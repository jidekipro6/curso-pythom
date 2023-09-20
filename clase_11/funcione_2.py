info={'dni':70522066,'nombre':'raul','apellido':'quijua','sexo':'Masculino','ciudad':'lima'},
{'dni':87654321,'nombre':'jideki','apellido':'torres','sexo':'Masculino','ciudad':'tumbes'},
{'dni':12345678,'nombre':'marco','apellido':'torner','sexo':'Masculino','ciudad':'callao'},
{'dni':11111111,'nombre':'rubi','apellido':'butstrap','sexo':'Femenino','ciudad':'arequipa'}


 
dni=int(input('ingrese DNI  :'))
dni_buscado = None
for clave, valor in info:
    if str(valor)==dni:
        dni_buscado=valor
        break
        
if dni_buscado is not None:
    print(f'el dato{dni}fue encontrado')   
else:
    print(f'el dato{dni} NO fue encontrado NO ESTA EN EL SISTEMA ')
 