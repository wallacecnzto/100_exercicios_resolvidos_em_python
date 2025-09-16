'''
39. Escreva um programa que exiba os números pares de 1 a 50 e os números ímpares de 51 a 100 utilizando um laço de repetição.
'''

for i in range(1, 51):
    if i % 2 == 0:
        print(f"Pares: {i}")
    else:
        print(f"Impares: {i}")