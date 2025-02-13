QtdNotas = input("Quantas notas você quer inserir?")

soma = 0
for n_nota_atual in QtdNotas:
    nota = input("Insira a nota ")
    soma = soma + nota

media = soma / QtdNotas
print("A média das notas é:", media)