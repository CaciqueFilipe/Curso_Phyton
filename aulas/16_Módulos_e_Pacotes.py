# Módulos e Pacotes
'''
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')

# agora vou remover e modularizar as funções em outro arquivo separado.
import sys
import os

# Adiciona o diretório '16_Modulos' ao path para que o Python consiga encontrar o arquivo 'uteis.py'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "16_Modulos")))

import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
'''

# Usando o pacote criado na pasta 16_Modulos/uteis_package
# agora vou remover e modularizar as funções em outro arquivo separado.
import sys
import os

# Adiciona o diretório '16_Modulos' ao path para que o Python consiga encontrar o arquivo 'uteis.py'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "16_Modulos")))
from uteis_package import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')




