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