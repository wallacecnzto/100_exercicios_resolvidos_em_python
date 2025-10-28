"""
Faça um programa que calcule e exiba a soma dos números pares de 1 a 100 utilizando um laço de repetição.
"""
eh_par = 0

# for i in range(1, 11):
#     if (i % 2 == 0):
#         eh_par += i
# print(eh_par)

for i in range(2, 11, 2):
    eh_par += i
print(eh_par)