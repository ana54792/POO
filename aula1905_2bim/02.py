from datetime import datetime
from zoneinfo import ZoneInfo
import locale
# from "nome do modulo" import "class"
#pode ser só "import datetime" mas vai ter que escrever mais vezes por exemplo "datetime.datetime" ao inves de botar from

x = datetime(2026, 5, 1) # variavel de data e hora
print(x)
print(type(x))

y = datetime(2026, 5, 19, 14, 30, 0) # ano, mes, dia, hora, minuto, segundo
print(y)
print(type(y))
# Pegar os valores separados:
print(type(y.day))
print(type(y.month))
print(type(y.year))
print(type(y.hour))
print(type(y.minute))
print(type(y.second))
print(type(y.date()))
print(type(y.time()))
print(type(y.weekday())) # 0 = segunda, terca= 1, quarta = 2, ...


# Define locale para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

#a = datetime.now(ZoneInfo("America/Sao_Paulo")) # pega a hora do fuso horario da cidade que você informar
#print(a)
z = datetime.now() # pega a hora do computador
print(z)
print(z.strftime("%d/%m/%Y, %H:%M:%S"))# %Y mostra 2026
print(z.strftime("%d/%m/%y, %H:%M:%S"))# %y mostra 26
print(z.strftime("%d/%m/%y - %A - %B - %H:%M:%S"))# %A dia da semana completo %a dia da semana mais curto / %B mes