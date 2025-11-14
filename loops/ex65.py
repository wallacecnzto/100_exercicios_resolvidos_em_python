# 65. Faça um programa que leia um vetor de números inteiros e verifique se ele está em ordem crescente.

tamanho_do_vetor = int(input("Digite o tamanho do vetor: "))
vetor = []
# vetor = [i for i in range(tamanho_do_vetor)]

for i in range(tamanho_do_vetor):
    elemento = int(input(f"Elemento {i + 1}: "))
    vetor.append(elemento)
    
eh_crescente = True

for i in range(1, tamanho_do_vetor): # começa da posição 1 para ir comparando com a posição anterior
    if vetor[i] < vetor[i - 1]:
        eh_crescente = False
        break
    
if eh_crescente:
    print("É crescente")
else:
    print("Não é crescente")
    