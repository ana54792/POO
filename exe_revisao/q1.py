class ContaDeAgua:
    def __init__(self):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
    def regras(self):
        if self.consumo <= 10:
            valor = 38
        elif self.consumo >= 11 and self.consumo <= 20:
            a_mais = self.consumo -10
            valor = 38 + (a_mais * 5)
        elif self.consumo >= 21:
            a_mais = self.consumo -20
            valor = 38 + 50 + (a_mais * 6)
        return valor



mes = int(input("Digite o mês da conta: "))
ano = int(input("Digite o ano da conta: "))
if mes <= 0 or mes >= 13:
    print("Mês inválido!!")
if ano < 2000:
    print("Ano inválido!!")
else:
    consumo = int(input("Digite o consumo de Água em m³: "))
    Conta = ContaDeAgua()
    valor = Conta.regras()
    print(f"Valor à ser pago = R${valor:.2f}")