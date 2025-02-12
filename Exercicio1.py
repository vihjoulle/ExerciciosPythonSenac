#1.	1.	Escreva um programa que peça o nome do usuário e exiba uma mensagem de boas-vindas.

nomeUser = input("Qual o seu nome? ")
genero = input("Você se identifica como homem ou mulher? (H/M): ").strip().upper()

if genero == "M":
    print(f"Olá {nomeUser}, seja bem-vinda!")
else:
    print(f"Olá {nomeUser}, seja bem-vindo!")