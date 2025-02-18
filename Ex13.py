#13. Leia um número e diga se ele é par ou ímpar.  

print("Vamos verificar se um número é par ou ímpar!")

try:
    numero_n = int(input("Entre com um número:"))

    if numero_n % 2 == 0:
        print(f"{numero_n} é par")
    else:
        print(f"{numero_n} é impar")

except ValueError:
    print("Erro: Você não digitou um número válido!")