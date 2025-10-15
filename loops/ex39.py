"""
39. Escreva um programa que exiba os números pares de 1 a 50 e os números
ímpares de 51 a 100 utilizando um laço de repetição.
"""

# for i in range(1, 51):
#    if i % 2 == 0:
#        print(f"Par: {i}")

for number in range(2, 50, 2):
    print(number)

print("=" * 10)

# for i in range(51, 101):
#     if i % 2 == 1:
#         print(f"Impar: {i}")

for number in range(51, 101, 2):
    print(number)
