"""
Escreva um programa que solicite ao usuário um número N e exiba a soma de todos os números de 1 a N.
"""
numero = int(input("Digite um número: "))
soma = 0

# for num in range(1, numero + 1):
#     soma = numero + num
#     print(f"soma de {numero} + {num} = {soma}")
    
for num in range(1, numero + 1):
    soma += num

print(f"A soma de todos os números de 1 a {numero} é: {soma}")
    