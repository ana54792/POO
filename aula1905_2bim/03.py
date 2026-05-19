from datetime import datetime


x = int(input("Informe um número: "))
print(x)

d = datetime.strptime(input("Informe uma data: "), "%d%m%Y") # o que vem depois da virgula mostra o padrao de numeros
print(d) #mostra d - m - ano 00:00:00
print(d.strftime("%d/%m/%Y")) # dizer como você quer ver nesse caso com os /

# strptime - passa o string para o datetime - método estatico - chama com a classe
# strftime - passa o datetime para o string - método de instancia - chama com uma variavel
#                                               da classe (objeto)