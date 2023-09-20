class persona:

    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def __str__(self):
        return self.nombre+" "+self.apellido+" de "+" "+str(self.edad )+ " años"

raul=persona("Raul","quijua",22)

print(raul)