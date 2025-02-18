#16. Peça três números e exiba-os em ordem crescente. 

print("""
    
█░█ ▄▀█ █▀▄▀█ █▀█ █▀   █▀█ █▀█ █▀▄ █▀▀ █▄░█ ▄▀█ █▀█   █▀█ █▀   █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█ █▀ ▀█
▀▄▀ █▀█ █░▀░█ █▄█ ▄█   █▄█ █▀▄ █▄▀ ██▄ █░▀█ █▀█ █▀▄   █▄█ ▄█   █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█ ▄█ ░▄
      
    """)

try:

    num_1 = int(input("Entre com o primeiro número: "))
    num_2 = int(input("Entre com o segundo número: "))
    num_3 = int(input("Entre com o terceiro número: "))

    if num_1 == num_2 == num_3:
        print("Todos os números digitados são iguais!")

    lista_Crescente= [num_1,num_2,num_3]
    lista_Crescente.sort()

    print(f"A ordem crescente dos números é {lista_Crescente}")
    
except ValueError:
    print("Entre com números válidos!")