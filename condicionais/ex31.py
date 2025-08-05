"""
31. Faça um programa que solicite o nome de um dia da semana e exiba se é um dia útil (segunda a sexta-feira) ou um dia
 de fim de semana (sábado e domingo).
"""
import unidecode # pip install unidecode para remover acentos.

dia_da_semana = input("Digite um dia da semana: ").lower()
dia_da_semana_sem_acentos = unidecode.unidecode(dia_da_semana)

if dia_da_semana == "sabado" or dia_da_semana == "domingo":
    print("Fim de semana!")
else:
    print("Dia útil!")