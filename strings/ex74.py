# 74. Escreva um programa que receba um nome e verifique se o mesmo começa com a letra "A".

nome = input("Digite um nome: ")

print(f"O nome {nome} começa com a letra A" if nome.startswith("A") else f"O nome {nome} não começa com a letra A")

# if nome[0].lower() == "a":
#     print("O nome começa com a letra A")
# else:
#     print("O nome não começa com a letra A")