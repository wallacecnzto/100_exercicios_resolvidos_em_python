"""
Escreva um programa que calcule o delta de uma equação de segundo grau (Δ = b² - 4ac).
"""
a = float(input("Digite o coeficiente de a: "))
b = float(input("Digite o coeficiente de b: "))
c = float(input("Digite o coeficiente de c: "))

delta = (b ** 2) - (4 * a * c)

print("O delta da equação de segundo grau é de: ", delta)