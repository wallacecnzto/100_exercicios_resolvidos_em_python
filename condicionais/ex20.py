"""
20. Faça um programa que leia um número e informe se ele é positivo, negativo ou zero.
"""
numero = int(input("Digite um número: "))

if numero > 0:
    print("Positivo!")
elif numero < 0:
    print("Negativo")
else:
    print("É zero!")