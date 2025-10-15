"""
40. Crie um programa que solicite ao usuário um número e exiba a tabuada desse número utilizando um laço de repetição.
"""
number = int(input("Digite um numero: "))

for i in range(1, 11):
    resultado = number * i
    print(f"{number} * {i} = {resultado}")
