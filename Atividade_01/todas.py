#1
print("Digite dois valores inteiros:")
n1 = int(input())
n2 = int(input())
if n2>n1:
    print(f"maior = {n2}")
elif n1 > n2:
    print(f"maior = {n1}")
elif n2 == n1:
    print("Números iguais")
     
#2

expressao = input("Digite dois valores inteiros separados por um operador +, -, * ou / (ex: 10 + 5): ")
lista = expressao.split()


num1 = int(lista[0])
operador = lista[1]
num2 = int(lista[2])


if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
   
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operador inválido"




print(f"O resultado da operação é: {resultado}")


#3
resultado_2 = 0
string = input("Digite uma frase:")
lista_2 = string.split()


for value in lista_2:
    if value.isnumeric():
        valor = value
       
        for i in valor:
            resultado_1 = int(i)
            resultado_2 += resultado_1
           
   
        print(resultado_2)


#4
resultado_3 = 0
print("Digite uma sequência de números separados por vírgula:")
string_2 = input()
lista_3 = string_2.split()


for value in lista_3:
    if True:
        valor_2 = value
       
        for i in valor_2:
            if i.isnumeric():
                resultado_4 = int(i)
                resultado_3 += resultado_4
           
   
        print(f"Soma = {resultado_3}")


#5
pais = input("Digite o nome do país:")
populacao = int(input("Digite sua população:"))
area = int(input("Digite sua área em km2::"))


densidade = populacao / area
print(f"A densidade demográfica do {pais} é de {densidade:.2f} hab/km2")

