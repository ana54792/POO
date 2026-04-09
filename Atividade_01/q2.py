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
