# 81. Faça um programa que preencha uma matriz 3x3 com valores informados pelo usuário e exiba a soma dos valores da diagonal principal.

# Criando a matriz
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Preenchendo a matriz com valores informados pelo usuário
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para sua posição [{i}][{j}]: "))

# Exibindo a matriz        
print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
    
# Calculando a soma da diagonal principal
soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]
    
print("Soma da diagonal principal:", soma_diagonal)