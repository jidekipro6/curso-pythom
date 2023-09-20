# Ejercicio 2: Herencia de Clase Empleado
# Crea una clase 'Empleado' con atributos 'nombre', 'edad' y 'salario'.
# Luego, crea otra clase 'Gerente' que herede de 'Empleado' y tenga un atributo adicional 'departamento'.

class Empleado:

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class Gerente(Empleado):

    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

empleado1 = Empleado("Juan", 18, 2000)
gerente1 = Gerente("Ana", 22, 3000, "Ventas")

print(f"Empleado: {empleado1.nombre}, Edad: {empleado1.edad}, Salario: ${empleado1.salario}")
print(f"Gerente: {gerente1.nombre}, Edad: {gerente1.edad}, Salario: ${gerente1.salario}, Departamento: {gerente1.departamento}")
