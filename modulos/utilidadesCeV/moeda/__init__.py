def aumentar(valor = 0, porcentagem = 0, formato=False):
    result = valor + (valor * porcentagem / 100)
    return result if formato is False else moeda(result)


def diminuir(valor = 0, porcentagem = 0, formato=False):
    result = valor - (valor * porcentagem / 100)
    return result if formato is False else moeda(result)


def dobro(valor = 0, formato=False):
    result = valor * 2
    return result if formato is False else moeda(result)


def metade(valor = 0, formato=False):
    result = valor / 2
    return result if formato is False else moeda(result)


def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')


def resumo(valor = 0, aumento = 0, reducao = 0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 30)


