#11.	Peça ao usuário uma frase e conte quantas vogais há nela.

frase = input("Entre com um frase:")
contador_vogais = 0

for caractere in frase:
     caractere = caractere.lower()
     if caractere in 'aeiou':
        contador_vogais += 1

print(f"Na frase, {frase} tem {contador_vogais} vogais")