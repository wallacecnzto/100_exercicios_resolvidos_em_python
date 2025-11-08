# Escreva um programa que solicite ao usuário dois números A e B e exiba todos os números entre A e B.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 >= num2:
    for i in range(num1, num2 - 1, -1):
        print(i)
else:
    for i in range(num1, num2 + 1):
        print(i)
