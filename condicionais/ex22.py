"""
22. Faça um programa que leia as notas de duas provas, calcule a média aritmética simples, e informe se o aluno foi
aprovado (média maior ou igual a 6) ou reprovado (média menor que 6).
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota_de_corte = 6.0
media = (nota1 + nota2) / 2.0

print("Aprovado! Sua nota foi {}".format(media)) if media >= nota_de_corte else print("Reprovado! Sua nota foi {}"
    .format(media))
