"""
Crie um programa que calcule e exiba a média aritmética de três notas informadas pelo usuário.
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_das_notas = (nota1 + nota2 + nota3) / 3

print("A média das 3 notas é {:.2f}".format(media_das_notas))