# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
item = 0
for mat in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite um valor para [{item},{c}]: '))
        matriz[item].append(valor)
    item += 1
print('-=' * 30)
for mat in range(0,3):
    for item in matriz[mat]:
        print(f'[ {item} ]', end='')
    print()
