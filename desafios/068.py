# Faça um programa que joga PAR ou Impar com o computador.
# O jogo só será interrompido quando o jogador perder
# Mostrando o total de vitórias consecutivas que ele conquistou no fnal do jogo
from random import randint
from time import sleep

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

vitorias = 0
while True:
    nJogador = int(input('Diga um valor: '))
    opcaoJogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if opcaoJogador not in 'PpIi':
        opcaoJogador = str(input('Opção inválida, tente Par ou Ímpar? [P/I] ')).upper().strip()[0]
    nComp = randint(0, 100)
    soma = nComp + nJogador
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'

    print('=-' * 20)
    print(f'Você jogou {nJogador} e o computador {nComp}. Total deu {soma} DEU {resultado}')
    print('=-' * 20)
    if resultado[0] == opcaoJogador:
        print('Você Venceu!')
        vitorias += 1
    else:
        break
    sleep(1)
    print('Vamos jogar novamente...')
    print('=-' * 20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')

vitorias = 0

# while True:
#     nJogador = int(input('Diga um valor: '))
#     opcaoJogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

#     nComp = randint(0, 100)

