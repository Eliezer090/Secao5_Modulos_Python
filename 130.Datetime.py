from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays
from calendar import monthrange

data = datetime(2019, 4, 20, 10, 53, 22)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# Adicionar 5 dias a data e segundos
data += timedelta(days=5, seconds=40)
print(data)

dt = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(dt)

print(dt.timestamp())
data = datetime.fromtimestamp(1555729200.0)
print(data)

d1 = datetime.strptime('20/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('22/06/2019 23:04:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1
print(dif)
print(dif.days)
print(d1.time())

# Data em portugues
setlocale(LC_ALL, 'pt_BR.utf-8')
dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y ')
print(formatacao)

# ULTIMO dia do mes
mes_atual = int(dt.strftime('%m'))
print(mdays[mes_atual])

#Ultimo dia do mes para ano Bisexto
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)
