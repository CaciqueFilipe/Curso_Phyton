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

