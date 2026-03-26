
class viagem:
    def __init__(self,km, tempo):
        self.km = km
        self.tempo = tempo
        pass
    def velocidade(self):
        self.velocidade = self.km//self.tempo
    def imprimir(self):
        print(f"A velocidade do carro na viagem foi de: {int(self.velocidade)}km/h")
    pass

veloc = viagem(200, 1.5)
veloc.velocidade()
veloc.imprimir()

veloc = viagem(200, 2)
veloc.velocidade()
veloc.imprimir()