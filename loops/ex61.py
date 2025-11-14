# Crie um programa que leia um vetor de números inteiros e exiba a soma de todos os elementos.

vetor = []
sum_vetor = 0

elementos = int(input("Digite a quantidade de elementos: "))
for element in range(elementos + 1):
    vetor.append(element)

for position in vetor:
    sum_vetor += position

print(sum_vetor)