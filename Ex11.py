#11. Verifique se um número é positivo, negativo ou zero.  
try:
    numero_Usuario = int(input("Entre com um número:"))

    if numero_Usuario == 0:
        print(f"{numero_Usuario} zerado")

    elif numero_Usuario <= 0:
        print(f"O número {numero_Usuario} é negativo")

    else:
        print(f"O {numero_Usuario} é positivo")
except:
    print("Entre com numero inteiros(Exemplos)")