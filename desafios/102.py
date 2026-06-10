# Crie um programa que tenha uma função fatorial() que receba dois parametro:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial
def fatorial(n, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    c = n
    f = 1
    resp = ''
    while c > 0:
        resp += str(c)
        if c > 1:
            resp += " x "
        else:
            resp += " = "
        f *= c
        c -= 1
    resp += str(f)
    if not show:
        resp = f

    return resp


print('-' * 30)
print(fatorial(5, True))
help(fatorial)

'''
# Gustavo
def fatorial(n, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-' * 30)
print(fatorial(5, True))
help(fatorial)
'''