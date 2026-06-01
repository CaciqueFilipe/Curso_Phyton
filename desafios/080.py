# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista.
# Já na posição correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada na tela

valores = list()

for cont in range(0, 5):
    valor =  int(input('Digite um valor: '))

    if cont == 0:
        valores.append(valor)
    else:
        print('Adicionado ')

        
print(f'Os valores digitados em ordem foram {valores}')