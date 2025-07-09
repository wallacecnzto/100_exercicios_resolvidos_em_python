"""
Escreva um programa que calcule a média geométrica entre três números informados pelo usuário
"""
import math

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media_geometrica = math.pow(num1 * num2 * num3, 1/3)

print("A média geométrica dos números é: {:.2f}".format(media_geometrica))