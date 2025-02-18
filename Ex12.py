#12. Peça dois números e informe qual é o maior.

print("Entre com dois números que vamos verificar qual é o maior.")

numero_1 = int(input("Entre com o primeiro numero:"))
numero_2 = int(input("Entre com o segundo número:"))

if numero_1 > numero_2:
    print(f"O {numero_1} é maior que o {numero_2}")

elif numero_2 > numero_1:
    print(f"O {numero_2} é maior que o {numero_1}")

else:
    print(f"O {numero_2} é igual o {numero_1}")