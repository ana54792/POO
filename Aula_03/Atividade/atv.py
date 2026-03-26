#Circulo
class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = 3.14 * (self.raio*self.raio)
        self.circ = 2* 3.14 * self.raio
        pass
    def imprimir(self):
        print(f"A área do circulo de raio = {self.raio} é: {self.area}")
        print(f"A circunferência do circulo de raio = {self.raio} é: {self.circ}")

    pass

circulo = Circulo(5)
circulo.imprimir()


