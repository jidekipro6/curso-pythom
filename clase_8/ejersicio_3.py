#Ejercicio 1: Registro de Notas
# Escribe un programa que permita al usuario ingresar nombres de estudiantes y sus respectivas notas. 
# El programa debe almacenar la información en un diccionario y finalizar cuando el usuario ingrese "fin".
# Al final, el programa debe mostrar el diccionario completo de estudiantes y sus notas.

alumno={}
mas_alumnos='si'

while mas_alumnos=='si':
    nombre=str(input("Ingrese el nombre :"))
    nota=int(input("ingrese nota :"))
    #alumno.update(nombre,nota)
    alumno[nombre] = nota 
     
    mas_alumnos=input("hay mas alumnos  si o no?")
print(f"los alumnos y sus notas son ",alumno)


 