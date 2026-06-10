# Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa
# Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(ano_nascimento: int):
    """
        -> Verifica se o ano recebido precisa votar nas eleicoes
        :param: int ano_nascimento
        :return: NEGADO, OPCIONAL ou OBRIGATÓRIO
    """
    from datetime import date

    idade = date.today().year - ano_nascimento
    print(f'Com {idade} anos: ', end='')
    if idade < 18:
        print('NÃO VOTA')
    elif 18 <= idade < 65:
        print('VOTO OBRIGATÓRIO')
    else:
        print('VOTO OPCIONAL')
    print()


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
