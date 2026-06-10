# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais.
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda, desenvolvida no desafio 108

import sys
import os

# Adiciona o diretório que contém o módulo 'moeda.py' ao sys.path.

caminho_modulo_moeda = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos', '107'))
sys.path.append(caminho_modulo_moeda)

import moeda

# Exemplo de uso (assumindo que moeda.py tem funções como aumentar, diminuir, etc.)
p = float(input('Digite o preço: R$ '))
print(f'Metade de {moeda.moeda(p)}: {moeda.metade(p, True)}')
print(f'Dobro de {moeda.moeda(p)}: {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)}: {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(p)}: {moeda.diminuir(p, 13, True)}')

