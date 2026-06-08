# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. (entre 1 e 6)
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = []
print('Valores sorteados:')
for c in range(1,5):
    jogador = {}
    jogador['nome'] = f'jogador{c}'
    jogador['dado'] = randint(1,6)
    print(f'{'':^4}O {jogador["nome"]} tirou {jogador["dado"]}')
    jogadores.append(jogador.copy())
    sleep(1.2)
print('Ranking dos jogadores:')
jogadores.sort('dado', Reverse=True)
for pos, jogador in jogadores.items():
    print(f'{'':^4}', f'{pos + 1}º lugar: {jogador['nome']} com {jogador['dado']}')
print()
