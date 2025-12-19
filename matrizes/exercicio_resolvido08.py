# Maior valor da matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

maior = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento

print(maior)

