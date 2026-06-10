# Crie um programa que tenha a função leiaInt()
# que vai funcionar de forma semelhante à função input() do Python
# só que fazendo a validação para aceitar apenas um valor númerico
#
# Ex:
# n = leiaInt('Digite um número')

def leiaInt(texto):
    """
    -> Função semelhante ao input, porém com validação para inteiro
    :param texto: texto da pergunta ao usuário
    """
    e_inteiro = False
    while not e_inteiro:
        try:
            n = int(input(texto))
            e_inteiro = True
        except Exception:
            print('ERRO! Digite um número inteiro válido.')
    return n


# Programa principal
print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')