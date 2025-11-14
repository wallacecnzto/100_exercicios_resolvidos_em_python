# 66. Escreva um programa que leia um vetor de números inteiros e exiba os elementos na ordem inversa.

tamanho_da_lista = int(input("Digite o tamanho do vetor: "))
lista = []

for i in range(tamanho_da_lista):
    elemento = int(input(f"Digite o {i + 1}º elemento: "))
    lista.append(elemento)
    
# lista.reverse() # modifica diretamente a lista, então não precisa retornar nada (None)

# print(lista)

# lista_invertida = lista[::-1] # sem modificar a original
# print(lista_invertida)

# lista_invertida = reversed(lista) # retorna um iterator do tipo objeto
# print(list(lista_invertida)) # converto de objeto para o tipo list antes de printar!

# invertendo no modo raiz
for i in range(tamanho_da_lista - 1, -1, -1):
    print(lista[i])