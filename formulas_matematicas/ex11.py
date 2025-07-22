"""
11. Escreva um programa que calcule a velocidade média de um objeto, utilizando a fórmula v = Δs/Δt, onde v é a
velocidade média, Δs é a variação de espaço e Δt é a variação de tempo
"""

variacao_de_espaco = float(input("Digite a variação de espaço: "))
variacao_de_tempo = float(input("Digite a variação de espaço: "))

velocidade_media = variacao_de_espaco / variacao_de_tempo

print(f"A velocidade média do objeto é de {velocidade_media:.2f}")
