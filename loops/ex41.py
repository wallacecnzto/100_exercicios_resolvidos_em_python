"""
41. Escreva um programa que imprima na tela a tabuada de todos os números de 1 a 10
"""
for number in range(1, 11):
    print("Tabuada do ", number)
    for i in range(1, 11):
        resultado = number * i
        print(number, "x", i, "=", resultado)
    print()