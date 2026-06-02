# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista.
# Já na posição correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada na tela
'''
valores = list()

for cont in range(0, 5):
    valor =  int(input('Digite um valor: '))

    if cont == 0:
        valores.append(valor)
    else:
        print('Adicionado ')

        
print(f'Os valores digitados em ordem foram {valores}')
'''
# Gustavo

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: # Se é maior que último elemento # ou elif n > lista[len(lista)-1]
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' *30)
print(f'Os valores digitados em ordem foram {lista}')
