# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma Sequência de Fibonacci
# Ex:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print("=" * 20)
print('SEQUENCIA DE FIBONACCI')
print("=" * 20)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print('{} -> {}'.format(t1, t2), end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')
