"""
15. Crie um programa que solicite ao usuário o valor do raio de uma esfera e calcule e exiba o seu volume.
Fórmula: V = (4/3) * pi * raio ao cubo.
"""
import math

raio = float(input("Digite o raio da esfera: "))
volume = (4 / 3) * math.pi * math.pow(raio, 3)

print(f"O valor do raio da esfera é de: {volume:.3f}")
