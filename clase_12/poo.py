class casa:
    def __init__(self,puerta,color,ventanas,altura,ancho):
        self.puerta=puerta
        self.color=color
        self.ventanas=ventanas
        self.altura=altura
        self.ancho=ancho

    def CasaCerrada(self):
        print('LA csa esta cerrada')
casa1=casa('si','naranja','2ventanas','3m','2m') 

casa1.CasaCerrada()
print(casa1.altura)