# Crie um programa que leia um vetor de números inteiros e verifique se todos os elementos são pares.

quantidade_de_elementos = int(input("Digite a quantidade de elementos: "))

lista = []

for i in range(quantidade_de_elementos):
    elemento = int(input(f"Digite o {i + 1}º elemento: "))
    lista.append(elemento)
    
todos_pares = True #começando a usar lógica booleana.

for i in lista:
    if i % 2 != 0:
        todos_pares = False
        break
    
print("Todos são pares!" if todos_pares else "Todos não são pares!")