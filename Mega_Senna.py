# -*- coding: utf-8 -*-
import random
from datetime import date
from datetime import datetime

linha='-'*57

text0 = 'Por: Izaias de Oliveira Elias '
text1 = 'Gerador de Dumeros Aleatorios da Mega-Sena'

a = random.sample(range(1,60),6)
b = random.sample(range(1,60),6)
c = random.sample(range(1,60),6)
d = random.sample(range(1,60),6)
e = random.sample(range(1,60),6)

print(linha)
print(text1.center(57,'*'))


x = datetime.now()
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
print("Hoje é", dias[x.weekday()])
print("Data",x.day,"/", x.month,"/", x.year)
print("Horas",x.hour ,":",x.minute,":",x.second)

print('\n','Os sorteios da Mega-Sena são realizados duas vezes por semana, às quartas e aos sábados.')

print('\n',dias[x.weekday()])
print(a)
print(b)
print(c)
print(d)
print(e)

print('\n','Boa sorte!')
print (linha)
print(text0.center(57,'*'))



