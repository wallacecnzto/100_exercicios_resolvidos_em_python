# Escreva um programa que leia números do usuário até que seja digitado um número negativo, e exiba a soma dos números positivos.

num = int(input("Digite um numero: "))
soma = 0

while num >= 0:
    soma += num
    num = int(input("Digite um numero: "))

print(soma)
