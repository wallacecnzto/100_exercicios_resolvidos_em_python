"""
19. Faça um programa que leia um número e informe se ele é par ou ímpar.
"""
numero = int(input("Digite o número: "))
#
# if numero % 2 == 0:
#     print("Par!")
# else:
#     print("Impar!")

print("Par") if numero % 2 == 0 else print("Impar!")