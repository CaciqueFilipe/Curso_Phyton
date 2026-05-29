# Desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla
# No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o valor 3.
# C) Quais foram os números pares.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')

n9 = 0
n3 = ''

for cont in range(0, len(valores)):
    if valores[cont] == 9:
        n9 += 1
    if n3 == '' and valores[cont] == 3:
        n3 = cont + 1
print(f'O valor 9 apareceu {n9} vezes')

if n3 != '':
    print(f'O valor 3 apareceu na {n3}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for cont in range(0, len(valores)):
    if valores[cont] % 2 == 0:
        print(valores[cont], end=' ')
print('\n')
'''
# Gustavo

núm = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor apareceu na {núm.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end="")
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
