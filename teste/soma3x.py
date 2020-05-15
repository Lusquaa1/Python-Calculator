from time import sleep

print('Você escolheu soma com três variáveis\n'
	'(a + b + c)')

somaA = float(input
	('Digite o valor de a:\n'))

somaB = float(input
	('Digite o valor de b:\n'))

somaC = float(input
	('Digite o valor de c:\n'))

Resultadosoma = (somaA + somaB + somaC)

print('\n')

print('Para receber um resultado arredondado da soma\n'
	  'entre os números {} + {} + {} , digite "A"'
	  .format(somaA, somaB, somaC))

print('\n')

print('Porém se quiser receber um resultado mais detalhado\n'
	'digite "B"')

sleep(1)
print('\n'
	'\n'
	'\n'
	'\n')
ops = 0

while not ops == 1000:
	ops = str(input
		('Digite a opção selecionada:'))

	if ops in 'Aa':
		print('O resultado arredondado da soma entre\n'
			'os números a = {}, b = {} e c= {}\n'
			'é igual a {:.0f}'
			.format(somaA, somaB, somaC, Resultadosoma))
		sleep(100)
		break

	if ops in 'Bb':
		print('O resultado arredondado da soma entre\n'
			'os números a = {},b = {} e c = {}\n'
			'é igual a {}'
			.format(somaA, somaB, somaC, Resultadosoma))
		sleep(100)
		break
