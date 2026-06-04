# Aprimore o desafio anterior, mostrando ao final:
# 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
item = 0
somapares = somaterceira = 0
for mat in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite um valor para [{item},{c}]: '))
        matriz[item].append(valor)
        if valor % 2 == 0:
            somapares += valor
        if c == 2:
            somaterceira += valor
    item += 1

print('-=' * 30)
for mat in range(0,3):
    for item in matriz[mat]:
        print(f'[ {item} ]', end='')
    print()

print('-=' * 30)
maiorvalor = max(matriz[1])
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maiorvalor}.')

'''
# Gustavo

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for lin in range(0,3):
    for c in range(0,3):
        matriz[lin][c] = int(input(f'Digite um valor para [{lin}, {c}]: '))
print('-=' * 30)
for lin in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[lin][c]:^5}]', end='')
        if matriz[lin][c] % 2 == 0:
            spar += matriz[lin][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for lin in range(0,3):
    scol += matriz[lin][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
'''
