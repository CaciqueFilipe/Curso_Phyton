lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1]) # suco
print(lanche[3]) # pudim
print(lanche[-2]) # pizza
# Pega a posição 1 e 2:
print(lanche[1:3]) # suco, pizza
# Começo na 2 até o final
print(lanche[2:]) # pizza, pudim
# Começo até antes da posição 2
print(lanche[:2]) # hamburguer, suco
# Começa no penultimo ate o final:
print(lanche[-2:]) # pizza, pudim

# Aqui vai dar erro:
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'

# Um print mais bonito

for comida in lanche:
    print(f'Eu vou comer {comida}')

# ou desta forma com range
'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
'''

# Depende do uso, exemplo se quiser mostrar a posicao, geralmente nem mostra, mas para diferenciar uso
'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
'''

# Se quisse usar o mesmo de cima:
'''
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
'''

print('Comi pra caramba!')

## Organizando a tupla
print(sorted(lanche)) # Coloca em ordem

## Outro exemplo, juntando tuplas:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) # quantas vezes aparece o numero 5
print(c.index(8)) # mostra em que posição está o 8 que aparece primeiro
print(c.index(5, 1)) # mostra em que posição está o numero 5 que aparece primeiro após a primeira posicao

# Python aceita qualquer tipo de variavel dentro da tupla:
pessoa = ('Filipe', 30, 'M', '80', '1.75')
print(pessoa)
# Deletando
del(pessoa)

# Se tentar acessar agora, da erro:
#print(pessoa)

# Não consigo deletar um item especifico:
# del(pessoa[0])
