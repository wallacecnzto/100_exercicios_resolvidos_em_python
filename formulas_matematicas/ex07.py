"""
Escreva um programa que calcule a área de um círculo a partir do raio, utilizando a fórmula A = πr²
"""
import math

raio = float(input("Digite o raio: "))

area = math.pi * (raio ** 2)

print("A área do círculo é de {:.2f}".format(area))
