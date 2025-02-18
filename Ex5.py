#5. Peça ao usuário sua idade e exiba o ano em que ele nasceu.  
try:
    idade_User = int(input("Qual a sua idade:"))
    Ano_atual = int(input("Entre com os 4 digitos do ano atual:"))

    ano_Nascimento = Ano_atual - idade_User

    print(f"Você nasceu em {ano_Nascimento} ou {ano_Nascimento - 1} ")

except:
    print("Dados Errados")