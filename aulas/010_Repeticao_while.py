# Comparando com FOR
'''
for c in range(1,10):
    print(c)
print('FIM')
'''

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

# Quando não sei o limite, o FOR não me atende

## Se quisesse no codigo abaixo que parasse quando digitasse 0
'''
for c in range(1,10):
    n = int(input('Digite um valor: '))
print('FIM')
'''

# O WHILE atende melhor neste cenário

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

# Ou perguntando ao usuário

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

# Outra situação em que eu tenha que pegar acontecimentos:

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))