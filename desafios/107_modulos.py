# Crie um módulo chamado moeda.py que tenha funçẽos incorporadas aumentar(), diminuir(), dobra() e metade()
#
# Faça também um programa que importe esse módulo e use algumas dessas funções

# agora vou remover e modularizar as funções em outro arquivo separado.

import sys
import os

# Adiciona o diretório que contém o módulo 'moeda.py' ao sys.path.

caminho_modulo_moeda = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos', '107'))
sys.path.append(caminho_modulo_moeda)

import moeda

# Exemplo de uso (assumindo que moeda.py tem funções como aumentar, diminuir, etc.)
p = float(input('Digite o preço: R$ '))
print(f'Metade de {p}: {moeda.metade(p)}')
print(f'Dobro de {p}: {moeda.dobro(p)}')
print(f'Aumentando 10% de {p}: {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13% de {p}: {moeda.diminuir(p, 13)}')

