# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de tres
# E que se encontram no intervalo entre 1 até 500

s = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('O somatório de todos os {} números impares entre 1 e 500 múltiplos de 3 é {}'.format(cont, s))