# 69. Escreva um programa que leia dois vetores de números inteiros com o mesmo tamanho e exiba um novo vetor com os elementos resultantes da multiplicação dos elementos correspondentes dos dois vetores.

tamanho_da_lista = int(input("Digite o tamanho das listas: "))

primeira_lista = []
segunda_lista = []
multiplicacao_entre_listas = []


for i in range(tamanho_da_lista):
    elemento_da_primeira_lista = int(input(f"Digite o {i + 1}º elemento da primeira lista: "))
    primeira_lista.append(elemento_da_primeira_lista)


print()


for i in range(tamanho_da_lista):
    elemento_da_segunda_lista = int(input(f"Digite o {i + 1}º elemento da segunda lista: "))
    segunda_lista.append(elemento_da_segunda_lista)


print()


for i in range(tamanho_da_lista):
    multiplicacao_entre_listas.append(primeira_lista[i] * segunda_lista[i])
    

print(multiplicacao_entre_listas)