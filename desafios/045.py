# Crie um programa que faça o computador jogar JokenPô com você

import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores
from time import sleep
from random import randint

fundoAmareloTextoVermelhoNegrito = cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"]
azulNegrito = cores["azul"]["azulNegrito"]
vermelhoNegrito = cores["vermelho"]["vermelhoNegrito"]
amareloNegrito = cores["amarelo"]["amareloNegrito"]
verdeNegrito = cores["verde"]["verdeNegrito"]
brancoNegrito = cores["branco"]["brancoNegrito"]
fundoBrancoTextoAzul = cores["branco"]["fundoBrancoTextoAzul"]
noColor = cores["limpa"]
fundoVermelhoTextoBranco = cores['vermelho']['fundoVermelhoTextoBranco']

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''{}Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
{}'''.format(
    fundoBrancoTextoAzul,
    noColor
))
jogador = int(input('{}Qual é a sua jogada?{}'.format(
    brancoNegrito,
    noColor
)))

if itens[jogador] == -1:
    print('{}Jogada inválida, tente novamente{}'.format(
        vermelhoNegrito,
        noColor
    ))
    exit()

print('{}JO{}'.format(
    fundoAmareloTextoVermelhoNegrito,
    noColor
))
sleep(1)
print('{}KEN{}'.format(
    fundoAmareloTextoVermelhoNegrito,
    noColor
))
sleep(1)
print('{}PO!!!{}'.format(
    fundoAmareloTextoVermelhoNegrito,
    noColor
))
sleep(1)
desenho = '-=' * 10

print('{}{}{}'.format(
    fundoBrancoTextoAzul,
    desenho,
    noColor
))
print('{}Computador jogou {}{}'.format(
    azulNegrito,
    itens[computador],
    noColor
))
print('{}Jogador jogou {}{}'.format(
    azulNegrito,
    itens[jogador],
    noColor
))

print('{}{}{}'.format(
    fundoBrancoTextoAzul,
    desenho,
    noColor
))

if computador == 0: #computador jogou PEDRA
    if jogador == 0: #jogador jogou PEDRA
        print('{}EMPATE{}'.format(
            amareloNegrito,
            noColor
        ))
    elif jogador == 1: #jogador jogou PAPEL
        print('{}JOGADOR VENCE{}'.format(
            verdeNegrito,
            noColor
        ))
    elif jogador == 2: #jogador jogou TESOURA
        print('{}COMPUTADOR VENCE{}'.format(
            vermelhoNegrito,
            noColor
        ))
    else:
        print('{}JOGADA INVÁLIDA!{}'.format(
            fundoVermelhoTextoBranco,
            noColor
        ))
elif computador == 1: #computador jogou PAPEL
    if jogador == 0: #jogador jogou PEDRA
        print('{}COMPUTADOR VENCE{}'.format(
            vermelhoNegrito,
            noColor
        ))
    elif jogador == 1: #jogador jogou PAPEL
        print('{}EMPATE{}'.format(
            amareloNegrito,
            noColor
        ))
    elif jogador == 2: #jogador jogou TESOURA
        print('{}JOGADOR VENCE{}'.format(
            verdeNegrito,
            noColor
        ))
    else:
        print('{}JOGADA INVÁLIDA!{}'.format(
            fundoVermelhoTextoBranco,
            noColor
        ))
elif computador == 2: #computador jogou TESOURA
    if jogador == 0: #jogador jogou PEDRA
        print('{}JOGADOR VENCE{}'.format(
            verdeNegrito,
            noColor
        ))
    elif jogador == 1: #jogador jogou PAPEL
        print('{}COMPUTADOR VENCE{}'.format(
            vermelhoNegrito,
            noColor
        ))
    elif jogador == 2: #jogador jogou TESOURA
        print('{}EMPATE{}'.format(
            amareloNegrito,
            noColor
        ))
    else:
        print('{}JOGADA INVÁLIDA!{}'.format(
            fundoVermelhoTextoBranco,
            noColor
        ))
