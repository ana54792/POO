#3
resultado = 0
string = input("Digite uma frase:")
lista = string.split()

for value in lista:
    if value.isnumeric():
        valor = value
        
        for i in valor:
            resultado1 = int(i)
            resultado += resultado1
            
    
        print(resultado)
