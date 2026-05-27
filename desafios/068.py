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
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'
    print('=-' * 20)
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {resultado}')
    print('=-' * 20)
    if resultado[0] == tipo:
        print('Você Venceu!')
        vitorias += 1
    else:
        break
    sleep(1)
    print('Vamos jogar novamente...')
    print('=-' * 20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')

