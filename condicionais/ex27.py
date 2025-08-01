"""
27. Faça um programa que leia três números e informe se eles podem ser os lados de um triângulo
(a soma de dois lados deve ser sempre maior que o terceiro lado).
"""

lado1 = int(input("Digite o primeiro número: "))
lado2 = int(input("Digite o segundo número: "))
lado3 = int(input("Digite o terceiro número: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados podem formar um triângulo!")
else:
    print("Os lados não podem formar um triângulo!")