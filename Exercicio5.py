#5.	Peça três números ao usuário e exiba a média deles.

n1 = float(input("Qual o primeiro número? "))
n2 = float(input("Qual o segundo número? "))
n3 = float(input("Qual o terceiro número? "))

ResultadoMedia = (n1 + n2 + n3) / 3

print(f"O resultado da média das notas é {ResultadoMedia:.2f}")