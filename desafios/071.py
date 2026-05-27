# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# E o programa vai informar quantas cédulas de cada valor serão entregues
#
# Obs.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.


print('=' * 20)
print('BANCO CEV')
print('=' * 20)

tot50 = tot20 = tot10 = tot1 = 0
valor = int(input('Que valor você quer sacar? R$ '))

while True:
    divisor = valor / 50


    if valor == 0:
        break

if tot50 > 0:
    print(f'Total de {tot50} cédulas de R$ 50')
if tot20 > 0:
    print(f'Total de {tot20} cédulas de R$ 20')
if tot10 > 0:
    print(f'Total de {tot10} cédulas de R$ 10')
if tot1 > 0:
    print(f'Total de {tot1} cédulas de R$ 1')

print('=' * 20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')