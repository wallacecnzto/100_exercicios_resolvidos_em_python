"""
Escreva um programa que calcule o perímetro e a área de um retângulo, utilizando as fórmulas P = 2(l + c) e A = lc, onde l é a largura e c é o comprimento
"""
largura = float(input("Digite a largura do retângulo e metros: "))
comprimento = float(input("Digite o comprimento do retângulo em metros: "))

perimetro = 2 * (largura + comprimento)
area = largura * comprimento

print(f"O perímetro do retângulo é de {perimetro} metros e a área é de {area} metros.")
