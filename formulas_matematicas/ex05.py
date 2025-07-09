"""
Escreva um programa que calcule o IMC de um indivíduo, utilizando a fórmula IMC = peso / altura²
"""
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print("Seu Índice de Massa Corporal (IMC) é de: {:.2f}".format(imc))