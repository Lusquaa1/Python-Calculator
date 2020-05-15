from time import sleep

print("Você selecionou cálculo de Divisão inteira!")

sleep(0.5)

print("Você poderá realizar divisões de 2 à 5 variáveis.")

OpcDivInt = 10

while OpcDivInt > 5:
    OpcDivInt = int(input("Selecione o número de variáveis a serem divididas\n"
                            "(Sendo ele de 2 à 5:"))

    if OpcDivInt == 2:
        import Divisaointeira2

        break
