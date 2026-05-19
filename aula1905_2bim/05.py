from datetime import datetime, timedelta

nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
hoje = datetime.now()

x = hoje - nasc
print(x)
y = x.days // 365
print(y, "anos")
m = x.days % 365 //30
print(m, "meses")
me = y * 12
print(me, "meses")