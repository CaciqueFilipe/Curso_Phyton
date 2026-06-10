# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionario com as seguinte informações
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings da função

def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional,  indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.

    """
    print('-'*30)
    maior = menor = tot = média = 0
    for cont, num in enumerate(n):
        if cont == 0:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        tot += num
    qtd_numeros = len(n)
    média = tot / qtd_numeros
    dados = {
        'total': qtd_numeros,
        'maior': maior,
        'menor': menor,
        'média': média
    }
    if sit:
        situação = 'BOA'
        if 7 > média >= 5:
            situação = 'RAZOÁVEL'
        elif média < 5:
            situação = 'RUIM'
        dados['situação'] = situação
    return dados


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)
help(notas)