"""
32. Escreva um programa que solicite a altura e o peso de uma pessoa e calcule o seu índice de massa corporal (IMC),
exibindo a categoria correspondente (abaixo do peso, peso normal, sobrepeso, obesidade, obesidade grave).
Menos de 18,5: Abaixo do peso
Entre 18,5 e 24,9: Peso normal
Entre 25 e 29,9: Sobrepeso
Entre 30 e 34: Obesidade
Acima de 35: Obesidade grave
Acima de 40: Obesidade mórbida
"""
import math

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / math.pow(altura, 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal.")
elif imc >= 25.0 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30.0 and imc <= 34:
    print("Obesidade.")
else:
    print("Obesidade grave.")