class Cidade:
    def __init__(self):
        self.__nome = ""
        self.__populacao = 0
        self.__area = 0
    def set_nome(self,no):
        if no != int and no != float: self.__nome = no
        else: ValueError("O valor informado deve ser em texto!")
    def set_populacao(self,pop):
        if pop >= 0: self.__populacao = pop
        else: ValueError("O valor deve ser positivo!")
    def set_area(self,lt):
        if lt >= 0: self.__area = lt
        else: ValueError("O valor deve ser positivo!")
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao // self.__area
    def __str__(self):
        return f"População = {self.__populacao} - Área = {self.__area} - Densidade = {self.densidade()}"

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op  = UI.menu()
            if op == 1: UI.calculo()

    @staticmethod
    def menu():
        print("1-Calculo 2-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def calculo():
        print("Calculo de densidade")
        c = Cidade()
        c.set_nome(input("Informe o nome da cidade: "))
        c.set_populacao(int(input("Informe a população da cidade: ")))
        c.set_area(int(input("Informe a área da cidade em km²: ")))
        densidade = c.densidade()
        print(f"Nome: {c.get_nome()}, População: {c.get_populacao()} habitantes, Área: {c.get_area()}, Densidade = {densidade}hab/km²")

UI.main()