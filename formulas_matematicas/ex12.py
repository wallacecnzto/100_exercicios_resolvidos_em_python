"""
12. Escreva um programa que calcule a energia cinética de um objeto em movimento, utilizando a fórmula E = (mv²) / 2,
onde E é a energia cinética, m é a massa do objeto e v é a velocidade.
"""
massa_do_objeto = float(input("Digite a massa do objeto: "))
velocidade_do_objeto = float(input("Digite a velocidade do objeto: "))

energia_cinetica = (massa_do_objeto * (velocidade_do_objeto ** 2)) / 2

print(f"A energia cinética calculada é de {energia_cinetica:.2f}")
