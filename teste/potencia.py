import math
from time import sleep

print('Você selecionou cálculo de potenciação!')

pt = float(input
	('Por favor digite o valor a ser potenciado:'))

#Fórmula

pt0 = (pt**0)

pt1 = (pt**1)

pt2 = (pt**2)

pt3 = (pt**3)

pt4 = (pt**4)

pt5 = (pt**5)

pt6 = (pt**6)

pt7 = (pt**7)

pt8 = (pt**8)

pt9 = (pt**9)

pt10 = (pt**10)

sleep(0.25)

print('As potências do número {:.1f}\n'
	'elevado ao expoente 0: {:.1f} \n'
	'elevado ao expoente 1: {:.1f} \n'
	'elevado ao expoente 2: {:.1f} \n'
	'elevado ao expoente 3: {:.1f} \n'
	'elevado ao expoente 4: {:.1f} \n'
	'elevado ao expoente 5: {:.1f} \n'
	'elevado ao expoente 6: {:.1f} \n'
	'elevado ao expoente 7: {:.1f} \n'
	'elevado ao expoente 8: {:.1f} \n'
	'elevado ao expoente 9: {:.1f} \n'
	'elevado ao expoente 10: {:.1f} \n'
	.format (pt, pt0, pt1, pt2, pt3, pt4, pt5,
		pt6, pt7, pt8, pt9, pt10))
print('Após 3 minutos o script será fechado automaticamente,'
	'Obrigado por testá-lo')
sleep(180)