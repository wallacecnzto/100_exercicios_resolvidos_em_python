# 77. Escreva um programa que receba um nome completo e exiba somente o primeiro nome.

nome_completo = input("Digite o nome completo: ")

lista_do_nome_completo = nome_completo.split()

primeiro_nome = lista_do_nome_completo[0]

print(primeiro_nome)