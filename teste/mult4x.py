import math
from time import sleep

print('Você escolheu multiplicação com quatro variáveis:')

ma = float(input
	('Digite o valor de a:'))

mb = float(input
	('Digite o valor de b:'))

mc = float(input
	('Digite o valor de c:'))

md = float(input
	('Digite o calor de d:'))

mabcd = (ma*mb*mc*md)

print('Para receber um resultado arredondado digite a')

sleep(0.25)

print('Para um resultado completo digite b')

sleep(0.25)

print('\n'
	'\n'
	'\n'
	'\n')

opm = 0

while not opm == 1000:
	opm = str(input('Opção selecionada :'))

	if opm in 'Aa':
		print('O resultado arredondado da multiplicação entre a = {},\n'
          'b = {}, c={} e d = {} é igual a {:.0f}'
          .format(ma, mb, mc, md, mabc))

	elif opm in 'Bb':
    	print('O resultado completo da multiplicação entre a = {},\n'
          'b = {}, c={} e d = {} é igual a {}'
          .format(ma, mb, mc, md, mabc))
