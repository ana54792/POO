class Retangulo:
    def __init__(self):
        self.__base = 0          #atributo encapsulado
        self.__altura = 0           #atributos
    def set_base(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__base = valor
    def get_base(self):
        return self.__base
    def set_altura(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__altura = valor
    def get_altura(self):
        return self.__altura
    def diagonal(self):             # métodos
        return (self.__altura**2 + self.__base**2) ** 0.5
    
# Programa principal
class UI:
    def main():
        R = Retangulo()

        R.set_altura (float(input("Digite a altura do retangulo ")))

        R.set_base (float(input("Digite a largura do retangulo ")))
        print(f"O retângulo de base = {R.get_base()} e altura {R.get_altura()}") 
        diagon = R.diagonal()
        print(f"Tem diagonal = {diagon}")

UI.main()
