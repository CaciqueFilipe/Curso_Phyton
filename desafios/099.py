# Faça um programa que tenha uma função chamada maior(), que receba varios parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
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

