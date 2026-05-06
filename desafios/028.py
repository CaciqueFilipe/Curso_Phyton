# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
# O programa deverá escrever na tela se o usuario venceu ou perdeu

from random import randint
from time import sleep
computador = randint(0,5)
print('{:=^20}'.format('JOGO DE ADIVINHAÇÃO'))
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))

from random import randint
from time import sleep

computador = randint(0,5) # Faz o computador "PENSAR"
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que numero eu pensei?")) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))
'''
