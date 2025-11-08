# Crie um programa que exiba os primeiros N numeros primos, onde N e informado pelo usuario, utilizando um laço de repetiçao.

N = int(input("Digite um numero inteiro N: "))

print(f"Os primeiros {N} numeros primos sao: ", numeros)

count = 0
num = 2

while count < N:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        coun += 1

    num += 1

