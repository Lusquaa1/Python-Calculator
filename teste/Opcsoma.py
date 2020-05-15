print('Você selecionou soma\n')

opcsoma = 10

while opcsoma > 5:
    opcsoma = int(input('Selecione o número de váriaveis a serem somadas\n'
                        'sendo eles de 2 a 5:'))
    if opcsoma == 2:
        import soma2x
    elif opcsoma ==3:
         import soma3x
    elif opcsoma ==4:
        import soma4x
    elif opcsoma ==5:
        import soma5x
    else:
        print('Por favor selecione um número de 2 a 5')