# 68. Faça um programa que leia um vetor de números inteiros e exiba quantas vezes um número específico aparece no vetor.

tamanho_da_lista = int(input("Digite o tamanho da lista: "))

lista = []

for i in range(tamanho_da_lista):
    item = int(input(f"Digite o {i + 1}º numero da lista: "))
    lista.append(item)
    

numero_especifico = int(input("Digite o número específico: "))

contador = 0

for i in lista:
    if numero_especifico == i:
        contador += 1


print(f"O número {numero_especifico} aparece {contador} vezes na lista.")
