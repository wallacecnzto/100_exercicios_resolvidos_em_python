# Conte quantos valores da matriz são maiores que 10.

matriz = [
    [5, 12, 7],
    [20, 3, 15]
]

contador = 0

for linha in matriz:
    for elemento in linha:
        if elemento > 10:
            contador += 1

print(contador)
