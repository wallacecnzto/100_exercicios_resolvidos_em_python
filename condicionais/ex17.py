""""
Faça um programa que leia dois números e informe qual é o maior.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == num2:
    print("São iguais!")
elif num1 > num2:
    print(f"O número {num1} é maior.")
else:
    print(f"O número {num2} é maior.")
