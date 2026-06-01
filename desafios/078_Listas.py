# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
#
# No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.


valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'Você digitou os valores: {valores}')
maior = max(valores)
print(f'O maior valor foi {maior} nas posições ', end='')
for cont, valor in enumerate(valores):
    if valor == maior:
        print(f'{cont}... ', end='')
menor = min(valores)
print(f'\nO menor valor foi {menor} nas posições ', end='')
for cont, valor in enumerate(valores):
    if valor == menor:
        print(f'{cont}... ', end='')
print()
