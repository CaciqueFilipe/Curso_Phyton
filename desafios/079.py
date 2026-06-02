# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# Caso o número já exista la dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente

'''
valores = []

resp = 'S'
while resp in 'S':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    
print('-=' *30)
print(f'Você digitou os valores {valores}')
'''
# Gustavo
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' *30)
números.sort()
print(f'Você digitou os valores {números}')
