from time import sleep

print('Você escolheu a soma com cinco variáveis\n'
	'(a + b + c + d + e)')

somaA = float(input
	('Digite o valor de a:\n'))

somaB = float(input
	('Digite o valor de b:\n'))

somaC = float(input
	('Digite o valor de c:\n'))

somaD = float(input
	('Digite o valor de d:\n'))

somaE = float(input
	('Digite o valor de e:\n'))

Resultadosoma = (somaA + somaB + somaC + somaD + somaE)

print('\n')

print('para receber um resultado arredondado da soma\n'
	'entre os números {} + {} + {} + {} + {} , digite "A"'
	.format(somaA, somaB, somaC, somaD, somaE))

print('\n')

print('Porém se quiser receber um resultado mais detalhado\n'
	'da soma, digite "B"')

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
			'os números a = {}, b = {}, c = {}, d = {} e e = {}\n'
			'é igual a {:.0f}'
			.format(somaA, somaB, somaC, somaD, somaE, Resultadosoma))
		sleep(100)
		break

	if ops in 'Bb':
		print('O resultado arredondado da soma entre\n'
			'os números a = {}, b = {}, c = {}, d = {} e e = {}\n'
			'é igual a {}'
			.format(somaA, somaB, somaC, somaD, somaE, Resultadosoma))
		sleep(100)
		break