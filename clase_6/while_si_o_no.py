asistencia=[]
hay_alguien_mas=input("hay algun alumno  (si / no: ) :")

while hay_alguien_mas=='si':
    alumno=input("Ingrese nombr de alumno :")
    asistencia.append(alumno)
    hay_alguien_mas=input("hay alguno alumno mas (si / no): ")
if asistencia:
    print(f"los alumnos son :{asistencia}")
else :
   print( "nadie vino se fueron d juerg ")
