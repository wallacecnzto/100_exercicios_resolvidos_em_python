"""
Faça um programa que leia a idade de três pessoas e quantas delas são maiores de idade.
"""

idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))
maioridade = 18
maiores_de_idade = 0

if idade1 >= maioridade:
    maiores_de_idade += 1

if idade2 >= maioridade:
    maiores_de_idade += 1

if idade3 >= maioridade:
    maiores_de_idade += 1

print("A quantidade de maiores de idade é de: ", maiores_de_idade)
