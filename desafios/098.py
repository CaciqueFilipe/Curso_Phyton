# Faça um programa que tenha uma função chamada contador(), que receba três parametros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
#
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    if inicio > fim:
        for c in range(inicio, fim, -passo):
            print(f'{c} ', end='')
            sleep(1)
        print('FIM!')
    else:
        for c in range(inicio, fim, passo):
            print(f'{c} ', end='')
            sleep(1)
        print('FIM!')


print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1,10,1)
print('-=' * 30)
print('De 10 até 0, de 2 em 2')
contador(10,0,2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 30)
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')