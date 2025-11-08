"""Escreva um programa que calcule e exiba o valor da potência de um número informado pelo usuário elevado a um expoente também informado pelo usuário, utilizando laços de repetição.
"""
# numero_informado = int(input("Digite um número: "))
# expoente_informado = int(input("Digite a potência desejada: "))
# potencia = 0

# while (numero_informado <= 0):
#     print("Número inválido, digite novamente: ")
#     numero_informado = int(input("Digite um número: "))

# while (expoente_informado <= 0):
#     print("Expoente inválido, digite novamente: ")
#     expoente_informado = int(input("Digite a potência desejada: "))

# potencia = numero_informado ** expoente_informado

# print(f"A potência de {numero_informado} é: {potencia}.")

numero = int(input("Digite o número base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
if expoente > 0:
    contador = 0
    while contador < expoente:
        resultado *= numero
        contador += 1
elif expoente < 0:
    contador = 0
    while contador > expoente:
        resultado /= numero
        contador -= 1
        
print(f"O resultado de {numero} elevado a {expoente} é: {resultado}")