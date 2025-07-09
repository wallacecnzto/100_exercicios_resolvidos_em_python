"""
1. Escreva um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print()

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"SOMA = {soma}\nSUBTRAÇÃO = {subtracao}\nMULTIPLICAÇÃO = {multiplicacao}")

if num2 != 0:
    divisao = num1 / num2
    print(f"DIVISÃO = {divisao}")
else:
    print("DIVISÃO = Não é possível a divisão por 0!")
