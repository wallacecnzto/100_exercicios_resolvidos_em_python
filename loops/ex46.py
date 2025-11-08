# Escreva um programa que solicite ao usuário um número N e exiba todos os números primos menores que N.

numero = (int(input("Digite um numero: ")))
eh_primo_menor_que_n = 0

if numero < 2:
    print(numero)
else:
    for i in range(2, numero + 1):
        if numero % i == 0:
            print(i)
