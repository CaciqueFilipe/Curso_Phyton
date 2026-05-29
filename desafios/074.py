# Crie um programa que vai gerar cinco números aleatórios em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

valores = (
    randint(0,20),
    randint(0,20),
    randint(0,20),
    randint(0,20),
    randint(0,20),
)
'''
maior = menor = 0
for cont in range(0, len(valores)):
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if maior < valores[cont]:
            maior = valores[cont]
        if menor > valores[cont]:
            menor = valores[cont]
print(f'OS valores sorteados foram: {valores}')
print(f'O maior valor entre eles foi {maior}')
print(f'O menor valor entre eles foi {menor}')
'''

# Guanabara
print('OS valores sorteados foram: ', end='')
for n in valores:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')