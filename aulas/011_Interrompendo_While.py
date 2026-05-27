'''
cont = 1
while True: # acontece para sempre ate um break
    print(cont, ' -> ', end='')
    cont += 1
print('Acabou')

'''

# Se temos algo assim e somamos, ele soma também o 999:

'''
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    # Interromper com break? Solução abaixo
    s += n
print('A soma vale {}'.format(s))
'''

# para ajustar isto, usamos break em um while infinito

n = s = 0
while True:
    n = int(input('Digite um número [999 para sair]: '))
    # Interromper com break? Solução abaixo
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
    