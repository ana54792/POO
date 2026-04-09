import math
class Retangulo:
    def __init__(self):
        self.altura = 0
        self.largura = 0
    def diagonal(self):
        return self.altura**2 + self.largura**2
    # return (self.altura**2 + self.largura**2) ** 0.5
    
R = Retangulo()
R.altura = int(input("Digite a altura do retangulo "))
R.largura = int(input("Digite a largura do retangulo "))
diagon = R.diagonal()
total = math.sqrt(diagon)
print(total)



#errado pq a raiz nem sempre é inteira
for i in range(diagon):
    raiz = i * i
    if raiz == diagon:
        print(i)
