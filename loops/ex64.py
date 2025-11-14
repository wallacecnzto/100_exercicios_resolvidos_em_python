# 64. Crie um programa que leia dois vetores de números inteiros com o mesmo tamanho e exiba um novo vetor
# com a soma dos elementos correspondentes dos dois vetores.

num = int(input("Digite o tamanho dos vetores: "))
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(num + 1):
    vetor1.append(i)
    
print(vetor1)

for x in range(num + 1):
    vetor2.append(x)

print(vetor2)

for y in range(num + 1):
    vetor3.append(vetor1[y] + vetor2[y])


print(vetor3)
