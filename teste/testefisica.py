##terceira lei de kepler

##fórmula = (T**2)/(R**3)

from time import sleep

opcao = 0

print("Bem vindo ao Script da Terceira lei de Kepler"),sleep(0.25)
print("para continuarmos, usaremos os seguintes dados,"),sleep(0.25)
print("o tempo de translação ( em segundos ),"),sleep(0.25)
print("e a distância entre os objetos (para obter um resultado em metros por segundos)"),sleep(0.25)
print("O conversor de unidades será iniciado..."),sleep(0.25)

while not opcao == "k":
    opcao = str(input ("Para cancelar a conversão de unidades digite k,para continuar insira quaquer letra\n"
        ":"))

    if opcao in 'Kk':
        print('Você pulou a conversão de unidades!')

    else:
        print("Você iniciou o modo de conversão de unidades!!")

##OPÇÕES

        print("Itens que podem ser convertidos :\n"
            "1 - Minutos para segundos\n"
            "2 - Horas para segundos\n"
            "3 - Dias para segundos\n"
            "4 - meses para segundos\n"
            "5 - anos para segundos\n"
            "6 - décadas para segundos")
        
        userconverse = 0

        while not userconverse == "k":
            
            opcaoconv = str(input("Para sair do modo de conversão de unidades digite k\n"
                ":"))
            
            if opcaoconv == 1:
                print("Você selecionou a conversão de unidades de minutos para segundos!"),sleep(0.25)
                print("Cada 1 minuto, contém 60 segundos.")
                
                convmin = int(input("Digite os minutos a serem convertidos para segundos"
                    ":"))

                minsec = (convmin * 60)

                print("Você converteu {} minutos para {}, peço que lembre do resultado para utilizarmos mais em frente".format(convmin,minsec))

            elif opcaoconv == 2:
                print("Você selecionou a conversão de unidades de horas para segundos!"),sleep(0.25)
                print("Cada 1 hora, contém 1440 segundos")

                convhrs = int(input("Digite as horas a serem convertidas para segundos\n"
                    ":"))


