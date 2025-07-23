"""
23. Faça um programa que leia três números, e informe se a soma deles é divisível por 5 ou não.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
soma_dos_numeros = num1 + num2 + num3

print("E divisível por 5") if soma_dos_numeros % 5 == 0 else print("Não é divisível por 5!")
