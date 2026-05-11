nome = str(input('Qual é o seu nome?'))

# Estrutura simples
'''
if nome == 'Filipe':
    print('Que nome bonito!')
print('Bom dia, {}!'.format(nome))
'''
## Exemplo reduzido
'''
print('Que nome bonito!' if nome == 'Filipe')
'''


# Estrutura composta
'''
if nome == 'Filipe':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal!')
print('Bom dia, {}!'.format(nome))
'''

# Estrutura condicional aninhada
'''
if nome == 'Filipe':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print('Bom dia, {}!'.format(nome))
'''

## E posso usar quantos elifs quiser
'''
if nome == 'Filipe':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Bom dia, {}!'.format(nome))
'''

## Pode ser sem o else no final
'''
if nome == 'Filipe':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')

print('Bom dia, {}!'.format(nome))
'''
