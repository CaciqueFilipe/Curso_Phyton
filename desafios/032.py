# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto
'''
A regra exata é:

O ano deve ser divisível por 4 (se dividirmos o ano por 4, o resto deve ser 0).

EXCEÇÃO: Se o ano for divisível por 100, ele não é bissexto...

EXCEÇÃO DA EXCEÇÃO: ...a menos que ele também seja divisível por 400.
'''

from time import sleep
ano = int(input("Digite um ano:"))
por4 = ano % 2
por100 = ano % 100
por400 = ano % 400
print('{:=^20}'.format('VERIFICANDO SE ANO É BISSEXTO...'))
sleep(2)

if (por4 == 0 and por100 != 0) or (por400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

'''
## Outra opção sugerida pelo Gustavo:
from datetime import date

print("\n{:=^20}".format(" Gustavo "))
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual:"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO".format(ano))
'''
