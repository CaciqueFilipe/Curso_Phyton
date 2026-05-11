# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# E mostre sua categoria de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER


import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores
from datetime import date

print('{}CATEGORIA DE NATAÇÃO?{}'.format(
    cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"],
    cores["limpa"]
))

atual = date.today().year
nasc = int(input('{}Ano de nascimento: {}'.format(
    cores['branco']['brancoNegrito'],
    cores['limpa']
)))
idade = atual - nasc
print('{}O atleta tem {} anos.{}'.format(
    cores['azul']['azulNegrito'],
    idade,
    cores['limpa']
))

categoria = ''

if idade <= 9:
    categoria = 'MIRIM'
    print('{}{}'.format(
        cores['verde']['fundoVerdeTextoBrancoNegrito'],
        cores['limpa']
    ))
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('{}Sua categoria é {}{}'.format(
    cores['verde']['fundoVerdeTextoBrancoNegrito'],
    categoria,
    cores['limpa']
))

