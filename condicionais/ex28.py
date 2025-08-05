"""
28. Faça um programa que leia o ano de nascimento de uma pessoa e informe se ela está apta a votar
(idade maior ou igual a 16 anos).
"""
ano_de_nascimento = int(input("Informe sua data de nascimento: "))
idade_para_votar = 16
#
# if ano_de_nascimento < idade_para_votar:
#     print("Você não pode votar!")
# else:
#     print("Você pode votar!")
print("Você pode votar!") if ano_de_nascimento >= idade_para_votar else print("Vocẽ não pode votar!")