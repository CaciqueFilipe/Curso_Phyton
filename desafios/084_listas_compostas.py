# Crie um programa que leia o nome e peso de várias pessoas
# Guardando tudo em uma lista. No final, mostre
#
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
mai= men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso Kg: ')))

    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'N':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
