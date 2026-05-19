# data e horario da aula de hoje: 19/05/2026 14:30 - datetime - instante de tempo
# tempo de duração da aula: 01:30                  - timedelta - intervalo de tempo

from datetime import datetime, timedelta

x = timedelta(hours = 1, minutes = 30)
print(x)

aula = datetime(2026, 5, 19, 14, 30)
print(aula)
print(aula.strftime("%d/%m/%Y %H:%M:%S")) # teste

print(aula + x)