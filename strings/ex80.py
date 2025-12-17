# 80. Escreva um programa que receba um nome completo e exiba o sobrenome (último nome) primeiro.

nome_completo = input("Digite o nome completo: ")

lista_nome_completo = nome_completo.split()

sobrenome = lista_nome_completo[-1]

print(f"O sobrenome é {sobrenome}")
