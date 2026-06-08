# Faça um programa que tenha uma função chamada contador(), que receba três parametros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
#
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
'''
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

'''
# Gustavo - Outra forma
from time import sleep

def contador(i, f, p):
    # validacao de negativo e 0
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) # Desliga buffer para sleep funcionar
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True) # Desliga buffer para sleep funcionar
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)