class Cinema:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario
    def calcular(self):
        if self.dia == "Segunda" or self.dia == "Terça" or self.dia == "Quinta":
            self.ingresso = 16
            self.meia = self.ingresso//2
            if self.horario >= 17:
                self.ingresso = self.ingresso + (self.ingresso/2)
                self.meia = self.ingresso//2
        if self.dia == "Quarta":
            self.ingresso = 8
            self.meia = 8
            if self.horario >= 17:
                self.ingresso = self.ingresso + (self.ingresso/2)
                self.meia = self.ingresso//2
        if self.dia == "Sexta" or self.dia == "Sábado" or self.dia == "Domingo":
            self.ingresso = 20
            self.meia = self.ingresso//2
            if self.horario >= 17:
                self.ingresso = self.ingresso + (self.ingresso/2)
                self.meia = self.ingresso//2
        

    pass

cinema = Cinema("Sexta", 13)
cinema.calcular()
print(f"O valor do ingresso é R${cinema.ingresso}")
print(f"O valor da meia-entrada é R${cinema.meia}")

cinema = Cinema("Sexta", 22)
cinema.calcular()
print(f"O valor do ingresso é R${cinema.ingresso}")
print(f"O valor da meia-entrada é R${cinema.meia}")

cinema = Cinema("Quarta", 14)
cinema.calcular()
print(f"O valor do ingresso é R${cinema.ingresso}")
print(f"O valor da meia-entrada é R${cinema.meia}")

cinema = Cinema("Quarta", 21)
cinema.calcular()
print(f"O valor do ingresso é R${cinema.ingresso}")
print(f"O valor da meia-entrada é R${cinema.meia}")

cinema = Cinema("Segunda", 11)
cinema.calcular()
print(f"O valor do ingresso é R${cinema.ingresso}")
print(f"O valor da meia-entrada é R${cinema.meia}")

cinema = Cinema("Segunda", 19)
cinema.calcular()
print(f"O valor do ingresso é R${cinema.ingresso}")
print(f"O valor da meia-entrada é R${cinema.meia}")