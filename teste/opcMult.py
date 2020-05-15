print('Você selecionou multiplicação\n')

opcmult = 10

while opcmult > 5:
    opcmult = int(input('Selecione o número de váriaveis a serem multiplicados\n'
                        'sendo eles de 2 a 5:'))
    if opcmult == 2:
        import multiplicação
    elif opcmult ==3:
         import multiplicação3x
    elif opcmult ==4:
        import multiplicação4x
    elif opcmult==5:
        import multiplicação5x
    else:
        print('Por favor selecione um número de 2 a 5')