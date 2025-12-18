# Crie uma matriz 3x3 preenchidas com zeros e mostre na tela.


matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(0)
    matriz.append(linha)


for linha in matriz:
    print(linha)


