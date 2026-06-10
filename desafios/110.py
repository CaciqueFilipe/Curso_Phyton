# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui

import sys
import os

# Adiciona o diretório que contém o módulo 'moeda.py' ao sys.path.

caminho_modulo_moeda = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos', '107'))
sys.path.append(caminho_modulo_moeda)

import moeda

# Exemplo de uso (assumindo que moeda.py tem funções como aumentar, diminuir, etc.)
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 80, 35)
