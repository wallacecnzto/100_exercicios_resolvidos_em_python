# 75. Faça um programa que leia uma palavra e verifique se a mesma é palíndromo (se pode ser lida da mesma forma de trás para frente).

palavra = input("Digite a palavra: ").lower()

if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é palíndromo.")
else:
    print(f"A palavra {palavra} não é palíndromo.")