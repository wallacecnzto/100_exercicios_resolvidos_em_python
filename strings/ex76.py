# 76. Crie um programa que leia duas palavras e verifique se a segunda palavra é um anagrama da primeira.

primeira_palavra = input("Digite a primeira palavra: ").lower()
segunda_palavra = input("Digite a segunda palavra: ").lower()

# Substitiu o espaço em branco da palavra por nada.
primeira_palavra.replace(" ", "")
segunda_palavra.replace(" ", "")

# Verifica se elas têm o mesmo tamanho.
if len(segunda_palavra) != len(primeira_palavra):
    print("As palavras não são anagramas.")
    
# Converte elas em listas.
lista_da_primeira_palavra = list(primeira_palavra)
lista_da_segunda_palavra = list(segunda_palavra)

# Ordena as listas (importante!)
lista_da_primeira_palavra.sort()
lista_da_segunda_palavra.sort()

# E compara se elas são iguais.
if lista_da_segunda_palavra == lista_da_primeira_palavra:
    print("A segunda palavra é anagrama da primeira palavra.")
else:
    print("A segunda palavra náo é anagrama da primeira palavra.")
    
