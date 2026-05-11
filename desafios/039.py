# Faça um programa que leia o ano de nascimento de uma jovem e informe, se acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
# Apenas para usar a pasta cores
import sys
import os
from time import sleep
# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores
from datetime import date

print('{}PRECISO ALISTAR?{}'.format(
    cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"],
    cores["limpa"]
))

atual = date.today().year
nasc = int(input('{}Ano de nascimento: {}'.format(
    cores['branco']['brancoNegrito'],
    cores['limpa']
)))
idade = atual - nasc
print('{}Quem nasceu em {} tem {} anos em {}.{}'.format(
    cores['azul']['azulNegrito'],
    nasc,
    idade,
    atual,
    cores['limpa']
))

if idade == 18:
    print('{}Você tem que se alistar IMEDIATAMENTE{}'.format(
        cores['verde']['fundoVerdeTextoBrancoNegrito'],
        cores['limpa']
    ))
elif idade < 18:
    print('{}Você ainda não tem 18 anos, faltam {} anos para o alistamento{}'.format(
        cores['verde']['fundoVerdeTextoBrancoNegrito'],
        18 - idade,
        cores['limpa']
    ))
elif idade > 18:
    print('{}Você já deveria ter se alistado há {} anos.{}'.format(
        cores['verde']['fundoVerdeTextoBrancoNegrito'],
        idade - 18,
        cores['limpa']
    ))