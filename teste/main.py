import hud1

user = 0
while not user == "k":
	user = input("digite k para sair: ")

	if user in "Aa":
		import Opcsoma

		break

	elif user in "Bb":
		import opcMult

		break

	elif user in "Cc":
		import potencia

		break

	else:
		print("Por favor digite uma opção válida!")
