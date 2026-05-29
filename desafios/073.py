# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol.
# Na ordem de colocação. Depois mostre :
#
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela;
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time do Corinthians

brasileirao_2026 = (
    'Palmeiras',
    'Flamengo',
    'Fluminense',
    'Athletico-PR',
    'Red Bull Bragantino',
    'Coritiba',
    'São Paulo',
    'Bahia',
    'Cruzeiro',
    'Botafogo',
    'Vitória',
    'Atlético-MG',
    'Internacional',
    'Grêmio',
    'Corinthians',
    'Vasco da Gama',
    'Santos',
    'Mirassol',
    'Remo',
    'Chapecoense'
)

print('-=' * 30)
print(f'Lista dos times do Brasileirão 2026: {brasileirao_2026}')
print('-=' * 30)
print(f'Os 5 primeiros são: {brasileirao_2026[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {brasileirao_2026[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(brasileirao_2026)}')
print('-=' * 30)
print(f'O Corinthinas está na {brasileirao_2026.index('Corinthians')}ª posição.')
