"""
35. Faça um programa que solicite dois números e exiba
se o primeiro é divisível pelo segundo.
"""
number_1 = int(input("Digite o primeiro número: "))
number_2 = int(input("Digite o segundo número: "))

print("Divisivel.") if number_1 % number_2 == 0 else print("Não é divisível.")
