# Calcule a soma da diagonal principal de uma matriz quadrada.
# 📌 Diagonal principal → quando linha == coluna (1 + 5 + 9)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_diagonal_principal = 0

for linha in range(len(matriz)):
    soma_diagonal_principal += matriz[linha][linha]

print("Soma diagonal:", soma_diagonal_principal)

