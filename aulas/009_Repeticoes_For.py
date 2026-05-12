# REPETINDO print 6 vezes:

for c in range(0, 6):
    print('Oi')
    # print(c) # aparece o contador
print('FIM')

# Para contar ao contrario:

for c in range(6, 0, -1):
    print('- Oi')
    # print(c) # aparece o contador
print('FIM')

# Pulando passos:

for c in range(0, 7, 2):
    print(c) # aparece o contador
print('FIM')

# Deixando usuário definir limite:

n = int(input('Digite um número: '))

for c in range(0, n + 1):
    print(c)
print('FIM')

# Deixando usuário definir todos:

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f + 1, p):
    print(c)
print('FIM')

# Pedindo 3 valores ao usuário:
for c in range(0,3):
    n = int(input('Digite um número: '))
print('FIM')


# Pedindo 3 valores ao usuário e somando eles:
s = 0
for c in range(0,4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os números é {}'.format(s))
