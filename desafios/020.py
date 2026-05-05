# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos.
# Faça um programa que leia o nome dos quatro alinos e mostre a ordem sorteada
import random

nome1 = input('Digite o nome do primeiro aluno:')
nome2 = input('Digite o nome do segundo aluno:')
nome3 = input('Digite o nome do terceiro aluno:')
nome4 = input('Digite o nome do quarto aluno:')
list = [
    nome1,
    nome2,
    nome3,
    nome4
]
random.shuffle(list)
print("A ordem de apresentação dos trabalhos será: {}".format(list))

'''
## Correção sugerida pelo Gustavo:

from random import shuffle

print("\n{:=^20}".format(" Gustavo "))
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')
list = [n1, n2, n3, n4]
shuffle(list)
print("A ordem de apresentação dos trabalhos será:")
print(list)
'''
