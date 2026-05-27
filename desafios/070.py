# Crie um programa que leia o nome e preço de varios produtos
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
#
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
totCompra = prodMais1000 = 0
prodMaisBarato = ''
preçoBarato = 0

while True:

    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))

    totCompra += preco
    if preco > 1000:
        prodMais1000 += 1
    if preçoBarato == 0:
        prodMaisBarato = nome
        preçoBarato = preco
    elif preco < preçoBarato:
        prodMaisBarato = nome
        preçoBarato = preco

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    
    if continuar in 'Nn':
        break
print('=' * 4, " FIM DO PROGRAMA ", '=' * 4)
print(f'O total da compra foi: R$ {totCompra:.2f}')
print(f'Temos {prodMais1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {prodMaisBarato} que custa R$ {preçoBarato:.2f}')

