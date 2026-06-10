# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# transfira todas as funções utilizadas nos desafios 107, 108 e 109  para o primeiro pacote e mantenha tudo funcionando.


import sys
import os

# Adiciona o diretório que contém o módulo 'moeda.py' ao sys.path.

caminho_modulo_moeda = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))
sys.path.append(caminho_modulo_moeda)

from utilidadesCeV import moeda

# Exemplo de uso (assumindo que moeda.py tem funções como aumentar, diminuir, etc.)
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 80, 35)
