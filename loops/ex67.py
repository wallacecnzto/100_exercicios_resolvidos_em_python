# 67. Crie um programa que leia um vetor de números inteiros e encontre o segundo maior elemento presente no vetor.

qtd_elementos_no_vetor = int(input("Digite a quantidade de elementos do vetor: "))

lista = []
elemento = 0

for i in range(qtd_elementos_no_vetor):
    print(f"Digite o {i + 1}º elemento: ")
    elemento = int(input())
    lista.append(elemento)

maior = lista[0]

for i in lista:
    if i > maior:
        maior = i

segundo_maior = float('-inf')

for i in lista:
    if i > maior:
        segundo_maior = maior # fazer a troca
        maior = i # fazer a troca
    elif i < maior and i > segundo_maior:
        segundo_maior = i

print()
print(f"Printando a lista: {lista}")
print(f"O primeiro maior valor é: {maior}")
print(f"O segundo maior valor é: {segundo_maior}")


