print("""
        𝕍𝕠𝕘𝕒𝕝 𝕠𝕦 𝕔𝕠𝕟𝕤𝕠𝕒𝕟𝕥𝕖❔
      """)

letra_Usuario = input("Entre com uma letra: ").lower()  # Tornar tudo minúsculo

# Verifica se a entrada é uma letra
if letra_Usuario.isalpha() and len(letra_Usuario) == 1:
    
    # Lista de vogais
    vogais = ["a", "e", "i", "o", "u"]

    # Verifica se a letra está na lista de vogais
    if letra_Usuario in vogais:
        print(f"A letra {letra_Usuario} é uma vogal.")
    else:
        print(f"A letra {letra_Usuario} é uma consoante.")

else:
    print("Você não digitou uma letra válida. Por favor, insira apenas uma letra.")
