class País():
    def __init__(self):
        self.nome = ""
        self.populacao = 1
        self.area = 1
        
    def calculo(self):
        return self.populacao / self.area
    
   
    
    
        
lista =[]
for k in range(10):  
    p = País()
    p.nome = input("Digite o nome do país:")
    p.populacao = int(input("Digite a população do país: "))
    p.area = int(input("Digite a área do país em Km²: "))
   
    densidade = p.calculo()
    lista.append(p)

maios = lista[0]
print(maios)
for i in lista:
    if i.calculo() > maios.calculo():
        maios = i
    
print(f"{maios.nome} é o país com a maior densidade, com {maios.calculo()} hab/km³")


