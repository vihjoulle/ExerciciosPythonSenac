#13.	Gere uma lista de 10 números aleatórios e exiba o maior e o menor número.

import random

GerarNum = input("Deseja gerar lista? (S/N): ").strip().upper()

if GerarNum == "S":
    lista_numeros = []
    for _ in range(10):  # Loop para gerar 10 números
        lista_numeros.append(random.randint(1, 100))  # Gera números entre 1 e 100 (ajuste conforme necessário)

    if lista_numeros:  # Verifica se a lista não está vazia
        maior_numero = max(lista_numeros)
        menor_numero = min(lista_numeros)

        print("Lista de números:", lista_numeros)
        print("Maior número:", maior_numero)
        print("Menor número:", menor_numero)
    else:
        print("Nenhum número foi gerado.")

elif GerarNum == "N":
    print("Geração de números cancelada.")

else:
    print("Opção inválida.")