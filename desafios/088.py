# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo.
# Cadastrando tudo em uma lista composta
'''
from random import randint
from time import sleep

print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)

qtd = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
jogo = []
print('-='*4, end='')
print(f' SORTEANDO {qtd} JOGOS ', end='')
print('-='*4)
for c in range(0, qtd):
    for j in range(0,6):
        while True:
            valor = randint(1,60)
            if valor not in jogo:
                jogo.append(valor)
                break
            
    jogos.append(jogo[:])
    print(f'Jogo {c + 1}: {jogo}')
    sleep(2)
    jogo.clear()
print('-='*4, end='')
print(' < BOA SORTE! > ', end='')
print('-='*4)

'''
# Gustavo
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, lin in enumerate(jogos):
    print(f'Jogo {i + 1}: {lin}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
