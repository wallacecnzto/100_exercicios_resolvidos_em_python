"""
14. Escreva um programa que leia a posição x e y de dois pontos no plano cartesiano, e calcule a distância entre ambos.
Lembre-se de que o teorema de Pitágoras nos permite calcular a distância entre dois pontos em um plano cartesiano usando
 as diferenças de coordenadas x e y e aplicando a fórmula da raiz quadrada.
"""
import math

coordenada_x1 = int(input("Digite a posição da coordenada X1: "))
coordenada_y1 = int(input("Digite a posição da coordenada Y1: "))

coordenada_x2 = int(input("Digite a posição da coordenada X2: "))
coordenada_y2 = int(input("Digite a posição da coordenada Y2: "))

dif_x = coordenada_x2 - coordenada_x1
dif_y = coordenada_y2 - coordenada_y1

distancia = math.sqrt(dif_x ** 2 + dif_y ** 2)

print("A distância entre os pontos é: {:.4f}".format(distancia))


