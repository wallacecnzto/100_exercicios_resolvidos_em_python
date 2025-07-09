"""
Escreva um programa que calcule o perímetro e a área de um triângulo, utilizando as fórmulas P = a + b + c e A = (b * h) / 2, onde a, b e c são os lados do triângulo e h é a altura relativa ao lado b.
"""
lado_a = float(input("Digite o tamanho do lado A do triângulo: "))
lado_b = float(input("Digite o tamanho do lado B do triângulo: "))
lado_c = float(input("Digite o tamanho do lado C do triângulo: "))
altura = float(input("Agora digite a altura do triângulo: "))

perimetro_triangulo = lado_a + lado_b + lado_c
area_do_triangulo = (lado_b * altura) / 2.0

print(f"O perímetro do triângulo é de {perimetro_triangulo} metros e a área é de {area_do_triangulo} metros.")
