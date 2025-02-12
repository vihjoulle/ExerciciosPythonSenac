#6.	Solicite um número e informe se ele é par ou ímpar.

numeroUsuario = int(input("Qual número você gostaria de saber? "))

if numeroUsuario % 2 == 0:
    print(f"O número {numeroUsuario} que você escolheu é par")
else:
    print(f"O número {numeroUsuario} que você escolheu é impar")