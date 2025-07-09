"""
Crie um programa que calcule e exiba o perímetro de um círculo, solicitando o raio ao usuário.
fórmula: P = 2 * pi * raio
"""
import math

raio = float(input("Digite o raio: "))

perimetro = 2 * math.pi * raio

print("O perímetro do círculo é de: {:.4f}".format(perimetro))