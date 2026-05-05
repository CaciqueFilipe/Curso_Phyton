# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random

nome1 = input('Digite o nome do primeiro aluno:')
nome2 = input('Digite o nome do segundo aluno:')
nome3 = input('Digite o nome do terceiro aluno:')
nome4 = input('Digite o nome do quarto aluno:')
# sorteado = random.choices([ #Errei o metodo aqui
sorteado = random.choice([  
        nome1,
        nome2,
        nome3,
        nome4
    ])

print("O escolhido foi: {}".format(sorteado))

'''
## Correção sugerida pelo Gustavo:

from random import choice

print("\n{:=^20}".format(" Gustavo "))
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')
lista = [
    n1,
    n2,
    n3,
    n4
]
sorteado = random.choice(lista)

print("O escolhido foi: {}".format(sorteado))
'''
