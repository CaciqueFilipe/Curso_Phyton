# Aprimore o desafio 093 para aquele que ele funcione com vários jogadores,
# Incluindo um sistema de vizualização de detalhes de aproveitamento de cada jogador

jogadores = []
while True:
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
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]')).upper()
    print('-' * 20)
    if resp in 'N':
        break
print(jogadores)
print('-=' * 30)
print(f'{"cod":<8}{"nome":<12}{"gols"}{"total":>20}')
print('-' * 45)
for i, j in enumerate(jogadores):
    print(f'{i:<8}{j["nome"]:<12}{j["gols"]}{j["total"]:>20}')
    print()
print('-' * 45)
while True:
    opc = int(input('Mostrar dados de qual jogador? '))
    existe = False
    for pos, jogador in enumerate(jogadores):
        if opc == pos:
            existe = True
            print('--', f'LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
            for j, g in enumerate(jogador["gols"]):
                print(f'{"":<5}No jogo {j} fez {g} gols.')
    if opc == 999:
        break
    if not existe:
        print(f'ERRO! Não existe jogador com código {opc}! Tente novamente')
    print('-' * 45)
print('<< VOLTE SEMPRE >>')


