#14. Verifique se um número é múltiplo de 5.  

print("""
      
      
𝕊𝕖𝕣𝕒́ 𝕢𝕦𝕖 𝕖𝕤𝕥𝕖 𝕟𝕦́𝕞𝕖𝕣𝕠 𝕖́ 𝕞𝕦𝕝𝕥𝕚𝕡𝕝𝕠 𝕕𝕖 𝟝❔

      """)
try:
    numero_User = int(input("Entre com um número: "))

    if numero_User % 5 == 0:
        print(f"O número {numero_User} é divisivel por 5.")

    else:
        print(f"O número {numero_User} não é divisivel por 5.")

except ValueError:
    print("Valor digitado invalido")