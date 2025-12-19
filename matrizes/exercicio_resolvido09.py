# Matriz como tabela (caso real)
# Crie uma matriz com nome e duas notas e calcule a média.

alunos = [
    ["Ana", 8.5, 7.0],
    ["João", 6.0, 9.0],
    ["Maria", 10.0, 9.5]
]

for aluno in alunos: # O iterator aluno é sempre uma lista!
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f"{nome} - Média {media:.2f}")

# Sempre que pensar em matriz, pense em 2 loops for...

# for linha in matriz:
#     for elemento in linha:
#         ...


# for i in range(linhas):
#     for j in range(colunas):
#         ...
