"""
25. Faça um programa que leia três números, e mostre eles na tela em ordem crescente.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num2 <= num1:
        meio = num2
        maior = num1
    else:
        meio = num1
        maior = num2

print(menor, meio, maior)

# Podemos usar as funções max() e min() também

menor = min(num1, num2, num3)
maior = max(num1, num2, num3)
meio = num1 + num2 + num3 - menor - maior

print("Os números em ordem crescente são: ", menor, meio, menor)
