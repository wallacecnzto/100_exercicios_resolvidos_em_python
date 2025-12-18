# Dada uma matriz, calcule a soma de todos os valores.

matriz = [
        [1, 2, 3],
        [4, 5, 6]
]

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento

print("Soma:", soma)
