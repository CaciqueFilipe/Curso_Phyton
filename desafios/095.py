# Aprimore o desafio 093 para aquele que ele funcione com vários jogadores,
# Incluindo um sistema de vizualização de detalhes de aproveitamento de cada jogador

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    qtd = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    tot = 0
    for p in range(0, qtd):
        gol = int(input(f'Quantos gols na partida {p + 1}? '))
        partidas.append(gol)
        tot += gol
    jogador['gols'] = partidas[:]
    jogador['total'] = tot
    time.append(jogador.copy())
    while True: # Validação de quer continuar:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
    print('-' * 20)
print(time)
print('-' * 40)
#cabecalho
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'ERRO! Não existe jogador com código {opc}! Tente novamente')
    else:
        print('--', f'LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}:')
        for i, g in enumerate(time[opc]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
