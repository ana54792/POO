# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2

class Circulo:
    def __init__(self):
        self.__raio = 0.0
        
    def set_raio(self, v):
        if v >= 0: self.__raio = v
        else: raise ValueError()
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14* (self.__raio**2)
    def calc_circunferencia(self):
        return 2 * 3.14 * self.__raio
class Viagem:
    def __init__(self):
        self.__quilometros = 0.0
        self.__tempo = 0.0
    def set_distancia(self, d):
        if d >= 0: self.__quilometros = d
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
    def get_distancia(self):
        return self.__quilometros
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__quilometros // self.__tempo
class Conta_Bancaria:
    def __init__(self):
        self.__nome = ""
        self.__numero = 0
        self.__saldo = 0
    def set_nome(self, n):
        if n == " ": raise ValueError()
        else: self.__nome = n
    def set_numero(self, num):
        if num >= 0: self.__numero = num
        else: raise ValueError()
    def set_saldo(self, s):
        if s >= 0: self.__saldo = s
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def deposito(self, va):
        self.__saldo += va
        print(f"Depósito de R${va} realizado.")
    def saque(self,va):
        if va > self.__saldo: print("Dinheiro insuficiente!")
        else: 
            self.__saldo -= va
            print(f"Saque de R${va} realizado.")

class Cinema:
    def __init__(self):
        self.__dia = ""
        self.__horario = 0
    def set_dia(self, d):
        if d == "Segunda" or d == "Terça" or d == "Quarta" or d == "Quinta" or d == "Sexta" or d == "Sabado" or d == "Domingo": self.__dia = d
        else: raise ValueError()
    def set_horario(self,h):
        if h >= 0 and h < 24: self.__horario = h
        else: raise ValueError()
    def get_dia(self):
        return self.__dia
    def get_horario(self):
        return self.__horario
    def inteira(self):
        if self.__dia == "Segunda" or self.__dia == "Terça" or self.__dia == "Quinta":
            self.__inteira = 16
            if self.__horario >= 17 and self.__horario < 24:
                self.__inteira += self.__inteira // 2
                return self.__inteira
            return self.__inteira
        elif self.__dia == "Sexta" or self.__dia == "Sabado" or self.__dia == "Domingo":
            self.__inteira = 20
            
            if self.__horario >= 17 and self.__horario < 24:
                self.__inteira += self.__inteira // 2
                return self.__inteira
            return self.__inteira
        elif self.__dia == "Quarta":
            self.__inteira = 8
            return self.__inteira
    def meia(self):
        if self.__dia == "Quarta":
            self.__meia = 8
            return self.__meia
        else:
            self.__meia = self.__inteira / 2
            return self.__meia



# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.cinema()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))     # método de instância
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print("Cálculo da área e circunferência do Circulo")
        y = Circulo()
        y.set_raio(float(input("Informe o valor do raio: ")))
        area_c = y.calc_area()
        circf = y.calc_circunferencia()
        print(f"Um circulo com raio {y.get_raio()} tem área = {area_c:.1f}cm² e circunferencia = {circf:.1f}")
    @staticmethod
    def viagem():
        print("Cálculo da velocidade média em um viagem")
        w = Viagem()
        w.set_distancia(int(input("Informe a distância percorrida: ")))
        w.set_tempo(int(input("Informe tempo - em horas - total da viagem : ")))
        velocidade = w.velocidade_media()
        print(f"Uma viagem de {w.get_distancia()} quilometros percorridos em {w.get_tempo()} horas foi feita em velocidade média de {velocidade}km/h")
    @staticmethod
    def conta_bancaria():
        print("Cálculo de saque e depósito")
        z = Conta_Bancaria()
        z.set_nome(input("Informe o nome do titular da conta: "))
        z.set_numero(int(input("Informe o número da conta: ")))
        z.set_saldo(float(input("Informe o saldo atual da conta: ")))
        print(f"O saldo atual da conta {z.get_numero()} é de R${z.get_saldo()}")
        z.saque(float(input("Informe o valor de saque: ")))
        print(f"O saldo atual da conta {z.get_numero()} é de R${z.get_saldo()}")
        z.deposito(float(input("Informe um depósito: ")))
        print(f"O saldo final da conta {z.get_numero()} é de R${z.get_saldo()}")
    @staticmethod
    def cinema():
        print("Cálculo de valor do ingresso de cinema")
        c = Cinema()
        c.set_dia(input("Informe o dia: "))
        c.set_horario(int(input("Informe o horário: ")))

        print(f"No dia {c.get_dia()} ás {c.get_horario()}h, o valor do ingresso inteiro é {c.inteira()} e a meia entrada é {c.meia()}")


UI.main()