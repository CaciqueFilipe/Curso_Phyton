# Faça um programa que tenha uma função chamada maior(), que receba varios parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*valores):
    print('Analisando os valores passados...')
    for v in valores:
        print(f'{v} ', end='')
    print(f'Foram informados {len(valores)} valores ao todo.')
    m = 0
    if len(valores) > 0:
        m = max(valores)
    print(f'O maior valor informado foi {m}')


print('-='*30)
maior(2,9,4,5,7,1)
print('-='*30)
maior(4,7,0)
print('-='*30)
maior(1,2)
print('-='*30)
maior(6)
print('-='*30)
maior()

'''
# Gustavo - Outra forma
from time import sleep

def maior(*núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True) # Desliga buffer para sleep funcionar
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
                


# Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()