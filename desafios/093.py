# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
qtd = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

gols = []
tot = 0
for p in range(0, qtd):
    gol = int(input(f'Quantos gols na partida {p}? '))
    gols.append(gol)
    tot += gol
jogador['gols'] = gols
jogador['total'] = tot

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {jogador['nome']} jogou {qtd} partidas')
for c in range(0, qtd):
    print(f'{'':^4}', f'=> Na partida {c + 1}, fez {jogador['gols'][c]} gols.')

print(f'Foi um total de {jogador['total']} gols.')
print()

