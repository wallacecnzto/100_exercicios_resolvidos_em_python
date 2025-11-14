# 62. Faça um programa que leia um vetor de números inteiros e exiba o maior elemento presente no vetor.

quantidade_de_numeros_do_vetor = int(input("Digite a quantidade de números do vetor: "))

vetor = [0 for i in range(quantidade_de_numeros_do_vetor)]
maior = vetor[0] # já inicia a variável com o valor do índice 0.

for elemento in range(quantidade_de_numeros_do_vetor + 1):
    if elemento > maior:
        maior = elemento

print(maior)
