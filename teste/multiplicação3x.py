import math
from time import sleep

ma = float(input
	('Digite o valor de a:'))

mb = float(input
	('Digite o valor de b:'))

mc = float(input
	('Digite o valor de c:'))

mabc = (ma*mb*mc)

print('Para receber um resultado arredondado digite a')

sleep(0.25)

print('Para um resultado completo digite b')

opm = str(input('Opção selecionada :'))

if opm in 'Aa':

    print('O resultado arredondado da multiplicação entre a = {},\n'
          'b = {} e c={} é igual a {:.0f}'.format(ma, mb, mc, mabc))

elif opm in 'Bb':

    print('O resultado completo da multiplicação entre a = {},\n'
          'b = {} e c={} é igual a {}'.format(ma, mb, mc, mabc))
