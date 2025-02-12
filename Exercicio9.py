#9.	Solicite um valor em reais e converta para dólares (suponha um câmbio fixo).

valorReais = float(input("Quantos reais você quer converter? "))
Cambio = 5.759

ValorAtualizado = valorReais * Cambio

print(f"O valor R$:{valorReais:.2f} em dolar é U$:{ValorAtualizado:.2f} ")