# Crie um programa que leia o nome e peso de várias pessoas
# Guardando tudo em uma lista. No final, mostre
#
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso Kg: ')))
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    pessoas.append(dados[:])
    dados.clear()
    if resp in 'N':
        break
listaMaior = []
listaMenor = []
for cont, p in range(0, len(pessoas)):
    if cont == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            maior = p[1]

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {}Kg. Peso de {}')
print(f'O menor peso foi de {}Kg. Peso de {}')