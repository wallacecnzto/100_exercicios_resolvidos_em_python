"""Escreva um programa que calcule e exiba o valor da potência de um número informado pelo usuário elevado a um expoente também informado pelo usuário, utilizando laços de repetição.
"""
numero_informado = int(input("Digite um número: "))
expoente_informado = int(input("Digite a potência desejada: "))
potencia = 0

for i in range(1, expoente_informado + 1):
    potencia = numero_informado * i
print(potencia)