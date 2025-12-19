# Somar todos os elementos

soma = 0

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

for linha in matriz:
    for elemento in linha:
        soma += elemento

print(soma)

