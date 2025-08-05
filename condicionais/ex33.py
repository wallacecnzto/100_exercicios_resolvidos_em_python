"""
33. Escreva um programa que solicite um número inteiro e verifique se é divisível por 3 e por 5 ao mesmo tempo.
"""
number = int(input("Digite um número inteiro: "))

if number % 3 == 0 and number % 5 == 0:
    print("É divisível.")
else:
    print("Não é divisível.")