# Ejercicio 3: Método Especial __str__
# Define una clase 'Libro' con atributos 'titulo', 'autor' y 'año'.
# Agrega un método especial __str__ para mostrar un mensaje personalizado cuando se imprime un objeto de la clase.
class libro:
    def __init__(self,titulo,autor,año):
        self.titulo=titulo
        self.autor=autor
        self.año=año

    def __str__(self):
        return f'titulo : {self.titulo} " --" su autor es : {self.autor} "--" el libro fue publiucado en el año :'
    


libro1=libro("QUIJOTE","MIGUEL DE CERVANTES SAVEDRA","1999")

print(libro1)    