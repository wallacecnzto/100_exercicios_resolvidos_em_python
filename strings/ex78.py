# 78. Faça um programa que receba uma frase e exiba a quantidade de espaços em branco presentes na mesma.

frase = input("Digite a frase: ")

# count() com intervalo (menos conhecido, mas útil)
# frase = "banana"
# print(frase.count("a", 2, 6))
# 👉 Conta "a" do índice 2 até o 5

quantidade_de_espacos_em_branco = frase.count(" ")

print(quantidade_de_espacos_em_branco)