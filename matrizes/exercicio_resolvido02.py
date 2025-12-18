# Leia uma matriz 2x2 digitada pelo usuário e exiba.

matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)


print("Matriz digitada:")
for linha in matriz:
    print(linha)
