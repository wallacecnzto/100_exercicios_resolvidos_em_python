# 79. Crie um programa que leia uma palavra e exiba a quantidade de vogais presentes na mesma.

palavra = input("Digite uma palavra: ")

vogais = 'aeiouAEIOU'
contador = 0

for caractere in palavra:
    if caractere in vogais:
        contador += 1
        
if contador == 0:
    print(f"A palavra {palavra} não possui vogais.")
else:
    print(f"A palavra {palavra} possui {contador} vogais.")