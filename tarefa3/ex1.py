class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0
        self.__litros = 0
    def set_destino(self,dest):
        if dest != int and dest != float: self.__destino = dest
        else: ValueError("O valor informado deve ser em texto!")
    def set_distancia(self,dist):
        if dist >= 0: self.__distancia = dist
        else: ValueError("O valor deve ser positivo!")
    def set_litros(self,lt):
        if lt >= 0: self.__litros = lt
        else: ValueError("O valor deve ser positivo!")
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia // self.__litros
    def __str__(self):
        return f"Distância = {self.__distancia} - Litros gastos ={self.__litros} - Consumo = {self.consumo()}"

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
        print("Calculo de consumo médio")
        v = Viagem()
        v.set_destino(input("Informe o nome do destino: "))
        v.set_distancia(int(input("Informe a distância percorrida em Km: ")))
        v.set_litros(int(input("Informe os litros de combustivel gastos na viagem: ")))
        consumo = v.consumo()
        print(f"Destino: {v.get_destino()}, Distância: {v.get_distancia()}km, Litros gastos: {v.get_litros()}, Consumo Médio = {consumo}km/l")

UI.main()