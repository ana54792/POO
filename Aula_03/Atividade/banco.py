class ContaBancaria:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        pass
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado.")
        pass
    def saque(self, valor):
        self.saldo -= valor
        print(f"Saque de R${valor} realizado.")
        pass
    
    pass

contabancaria = ContaBancaria('Jessica', 76427, 30)
contabancaria.deposito(200)
contabancaria.saque(50)
contabancaria.saque(185)

print(f"Saldo final: {contabancaria.saldo}")