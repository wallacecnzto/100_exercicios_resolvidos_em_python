"""
24. Crie um programa que leia três números e verifique se a soma deles é positiva, negativa ou igual a zero
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
soma = num1 + num2 + num3

if soma > 0:
    print("É positivo!")
elif soma < 0:
    print("É negativo")
else:
    print("É igual a zero!")
