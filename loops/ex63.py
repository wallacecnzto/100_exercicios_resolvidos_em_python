# 63. Escreva um programa que leia um vetor de números inteiros e exiba a média dos elementos.

num = int(input("Digite a quantidade de números do vetor: "))

# vetor = [0 for i in range(num)]
vetor = []

for i in range(num + 1):
    vetor.append(i)

soma = sum(vetor)
print(vetor)
print(soma)
media  = soma / num

print(f"A média de {num} elementos é {media}")

