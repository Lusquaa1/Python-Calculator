from time import sleep

print('Você escolheu soma com duas váriaveis\n'
      '( a + b )')

somaA = float(input('Digite o valor de a\n:'
                    ''))

somaB = float(input('Digite o valor de b\n:'
                    ''))

Resultadosoma = (somaA + somaB)

print('Para receber um resultado arredondado da soma\n'
      'entre os números {} + {} digite A\n'
      .format(somaA, somaB))

print('Ou para um resultado mais detalhado da soma\n'
      'digite B\n')
sleep(2)
print('\n'
      '\n'
      '\n'
      '\n')
ops = 0

while not ops == 1000:
    ops = str(input('Digite a opção selecionada\n:'))

    if ops in 'Aa':
        print('O resultado arredondado da soma entre\n'
              'os números a ={} e b ={} é igual a {:.0f}'
              .format(somaA, somaB, Resultadosoma))
        sleep(100)
        break

    elif ops in 'Bb':
        print('O resultado detalhado da soma entre\n'
              'os números a = {} e b = {} é igual a {}'
              .format(somaA, somaB, Resultadosoma))
        sleep(100)
        break
