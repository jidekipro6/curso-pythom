info = [
    {'dni': 70522066, 'nombre': 'raul', 'apellido': 'quijua', 'sexo': 'Masculino', 'ciudad': 'lima'},
    {'dni': 87654321, 'nombre': 'jideki', 'apellido': 'torres', 'sexo': 'Masculino', 'ciudad': 'tumbes'},
    {'dni': 12345678, 'nombre': 'marco', 'apellido': 'torner', 'sexo': 'Masculino', 'ciudad': 'callao'},
    {'dni': 11111111, 'nombre': 'rubi', 'apellido': 'butstrap', 'sexo': 'Femenino', 'ciudad': 'arequipa'}
]

dni = int(input('Ingrese DNI: '))

dni_encontrado = 0
for persona in info:
    if persona['dni'] == dni:
        dni_encontrado = persona
        break

if dni_encontrado is not None:
    print(f'El dato DNI {dni} fue encontrado en el sistema. Datos de la persona:')
    print(f'Nombre: {dni_encontrado["nombre"]}')
    print(f'Apellido: {dni_encontrado["apellido"]}')
    print(f'Sexo: {dni_encontrado["sexo"]}')
    print(f'Ciudad: {dni_encontrado["ciudad"]}')
else:
    print(f'El dato DNI {dni} NO fue encontrado en el sistema.')