from time import sleep

print('Você escolheu a soma com quatro variáveis\n'
	'(a + b + c + d)')

somaA = float(input
	('Digite o valor de a:\n'))

somaB = float(input
	('Digite o valor de b:\n'))

somaC = float(input
	('Digite o valor de c:\n'))

somaD = float(input
	('Digite o valor de d:\n'))

Resultadosoma = (somaA + somaB + somaC + somaD)

print('\n')

print('para receber um resultado arredondado da soma\n'
	'entre os números {} + {} + {} + {} , digite "A"'
	.format(somaA, somaB, somaC, somaD))

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
		print('O resultado arrendondado da soma entre\n'
			'os números a = {}, b = {}, c = {} e d = {}\n'
			'é igual a {:.0f}'
			.format(somaA, somaB, somaC, somaD, Resultadosoma))
		sleep(100)
		break

	if ops in 'Bb':
		print('O resuldado arredondado da soma entre\n'
			'os números a ={}, b = {}, c = {} e d = {}\n'
			'é igual a {}'
			.format(somaA, somaB, somaC, somaD, Resultadosoma))
		sleep(100)
		break