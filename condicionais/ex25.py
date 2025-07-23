"""
25. Faça um programa que leia três números, e mostre eles na tela em ordem crescente.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 and num1 < num3:
    primeiro_menor = num1
elif num2 < num3 and num2 < num1:
    segundo_menor = num2
else:
    terceiro_menor = num3

print(primeiro_menor, segundo_menor, terceiro_menor)

