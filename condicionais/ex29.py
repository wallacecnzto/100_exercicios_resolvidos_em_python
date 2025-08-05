"""
29. Faça um programa que leia a idade de uma pessoa e informe se ela não está apta a votar (idade inferior a 16 anos),
 se está apta a votar, porém não é obrigada (16, 17 anos, ou idade igual ou superior a 70 anos), ou se é obrigada
  (18 a 69 anos).
"""
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não está apto a votar!")
elif idade >= 16 and idade <= 17:
    print("É opcional entre 16 a 17 anos.")
elif idade >= 18 and idade < 70:
    print("É obrigatório o votar!")
else:
    print("É opcional na senioridade acima de 69 anos.")
