"""
34. Crie um programa que solicite a idade de uma pessoa e exiba se ela é criança (0-12 anos), adolescente (13-17 anos),
 adulto (18-59 anos) ou idoso (60 anos ou mais).
"""
age = int(input("Digite a idade: "))

if age <= 12:
    print("Criança.")
elif age >= 13 and age <= 17:
    print("Adolescente.")
elif age >= 18 and age <= 59:
    print("Adulto.")
else:
    print("Idoso.")