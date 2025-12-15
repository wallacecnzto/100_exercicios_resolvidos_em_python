# 76. Crie um programa que leia duas palavras e verifique se a segunda palavra é um anagrama da primeira.

primeira_palavra = input("Digite a primeira palavra: ").lower()
segunda_palavra = input("Digite a segunda palavra: ").lower()
eh_anagrama = False

if len(segunda_palavra) == len(primeira_palavra):
    eh_anagrama = True

for letra in segunda_palavra:
    if letra in primeira_palavra:
        eh_anagrama = True
        
if 