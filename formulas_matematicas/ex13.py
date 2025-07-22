"""
13. Escreva um programa que calcule o trabalho realizado por uma força que atua sobre um objeto, utilizando a fórmula
T = F * d, onde T é o trabalho, F é a força aplicada e d é a distância percorrida pelo objeto.
"""
forca_aplicada = float(input("Digite a força aplicada: "))
distancia_percorrida = float(input("Digite a distância percorrida: "))

trabalho = forca_aplicada * distancia_percorrida

print(f"O trabalho realizado por uma força que atua sobre um objeto é de {trabalho:.2f} joules.")
