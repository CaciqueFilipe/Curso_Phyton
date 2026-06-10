# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado

import sys
import os

# Adiciona o diretório que contém o módulo 'moeda.py' ao sys.path.

caminho_modulo_moeda = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos', '107'))
sys.path.append(caminho_modulo_moeda)

import moeda

# Exemplo de uso (assumindo que moeda.py tem funções como aumentar, diminuir, etc.)
p = float(input('Digite o preço: R$ '))
print(f'Metade de {moeda.moeda(p)}: {moeda.moeda(moeda.metade(p))}')
print(f'Dobro de {moeda.moeda(p)}: {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)}: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13% de {moeda.moeda(p)}: {moeda.moeda(moeda.diminuir(p, 13))}')

