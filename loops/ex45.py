"""Escreva um programa que solicite ao usuário um número N e diga se o mesmo é primo ou não. Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo, sem ter outros divisores.
Um número é considerado primo quando ele é maior que 1 e possui apenas dois divisores inteiros positivos:
👉 1 e ele mesmo.
Ou seja, um número primo não pode ser dividido exatamente (sem resto) por nenhum outro número além de 1 e dele próprio.
🔢 Exemplos:
2 é primo → divisores: 1 e 2
3 é primo → divisores: 1 e 3
4 não é primo → divisores: 1, 2 e 4
5 é primo → divisores: 1 e 5
9 não é primo → divisores: 1, 3 e 9
"""

numero = int(input("Digite um número: "))
contador = 0

if numero < 2:
    print("Não é primo!")
else:
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    print("É primo!" if contador <= 2 else "Não é primo!")
