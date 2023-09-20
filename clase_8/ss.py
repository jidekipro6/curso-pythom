alumnos = {}

while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")

    if nombre.lower() == 'fin':
        break

    nota = input(f"Ingrese la nota para {nombre}: ")
    alumnos[nombre] = nota

print("\nRegistro de Notas:")
for nombre, nota in alumnos.items():
    print(f"{nombre}: {nota}")