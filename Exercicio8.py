#8.	Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

numeroUsuario = int(input("Qual número você quer saber a tabuada?" ))

for i in range(1,11):
    resultadotabuada = numeroUsuario * i
    print(f"O resultado da tabuada do {numeroUsuario} x {i} = {resultadotabuada}")