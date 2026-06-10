# Crie um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome_do_jogador = '', gols = 0):
    """
    -> Função para exibir números do jogador
    :param nome_do_jogador: (opcional) nome do atleta
    :param gols: (opcional) quantidade de gols
    """
    if nome_do_jogador == '':
        nome_do_jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome_do_jogador} fez {gols} gol(s) no campeonato.')


print('-' * 30)
jogador = input('Nome do Jogador: ')
gols = input('Numero de gols: ')

ficha(jogador, gols)

