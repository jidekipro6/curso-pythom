class persona:

    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

raul=persona("Raul","quijua","22")

print(f"el nombre de usuario {raul.nombre} y su apellido es {raul.apellido} con una edad de {raul.edad} AÑOD")
