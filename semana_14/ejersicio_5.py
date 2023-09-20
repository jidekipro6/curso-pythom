

class Universidad:

    def __init__(self,DirecUni,NonUni,SedeUni):
        self.DirecUni=DirecUni
        self.NonUni=NonUni
        self.SedeUni=SedeUni
    def __str__(self):
        return f'Universidad {self.DirecUni} - {self.NonUni} - {self.SedeUni}'


class Departamanento:

    def __init__(self,NroDepa,NivelDepa,PrecioDepa,universidad):
        self.NroDepa=NroDepa
        self.NivelDepa=NivelDepa
        self.PrecioDepa=PrecioDepa
        self.universidad=universidad
    def __str__(self):
        return f'Departamento {self.NroDepa} - {self.NivelDepa} - {self.PrecioDepa}- {self.universidad.DirecUni}- {self.universidad.NonUni}- {self.universidad.SedeUni}'

universidad=Universidad("AV los postes 45 ","Universidad Teclogica del Peru","lima")
departamanento=Departamanento("Nro 5 ","3 pisi","1.200",universidad)  
print(departamanento)
print(departamanento.universidad)
  