"""
21. Faça um programa que leia as notas de duas provas e informe se o aluno foi aprovado (nota maior ou igual a 6) ou
reprovado (nota menor que 6) em cada uma das provas.
"""
prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
nota_de_corte = 6
print()
print("Aprovado na primeira prova!") if prova1 >= nota_de_corte else print("Reprovado na primeira prova!")
print("Aprovado na segunda prova!") if prova2 >= nota_de_corte else print("Reprovado na segunda prova!")
