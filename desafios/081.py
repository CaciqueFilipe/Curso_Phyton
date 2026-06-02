# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma descrescente
# C) Se o valor 5 foi digitado e está ou nçao na lista
'''
valores = []

resp = 'S'
while resp in 'S':
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    
print('-=' *30)
print(f'Você digitou {len(valores)} elementos.')
decres = valores.sort(reverse=True) # aqui não atribui
print(f'Os valores em ordem decrescente são {decres}.')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')

'''
# Gustavo
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' *30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')