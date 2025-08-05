"""
Faça um programa que leia três notas de um aluno e informe se ele foi aprovado (nota final maior ou igual a 7),
 reprovado (nota final menor que 4) ou ficou de recuperação (nota final entre 4 e 7).
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media < 4:
    print("Reprovado!")
elif media >= 4 and media <= 7:
    print("Recuperação!")
else:
    print("Aprovado!")