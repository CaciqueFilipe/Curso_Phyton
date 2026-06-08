pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '32'}
print(pessoas)
#print(pessoas[0]) #ERROO
print(pessoas['nome']) # Gustavo
print(pessoas['idade']) # 32
# Para imprimir formatado
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # Cuidado aspas simples e duplas

print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # dict_values(['Gustavo', 'M', '32'])
print(pessoas.items()) # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', '32')
print()

# Acessando por laços
for k in pessoas.keys():
    print(k)

# Ou :
print()
for v in pessoas.values():
    print(v)
print()

# Se quiser bonito com chave e valor:
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Apagando algo:
del pessoas["sexo"]
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Trocando algo:
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Adicionando elemento
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()


# Criando dicionario dentro de lista
print('-'* 6, f'{' Dicionario dentro de lista ':^4}', '-'*6)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print()
print(brasil[0]) # estado1
print(brasil[1]) # estado2
print(brasil[0]['uf']) # Rio de Janeiro
print(brasil[1]['sigla']) # SP

# Pequeno problema !!!
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #brasil.append(estado) # Assim ele não fará a copia
    #brasil.append(estado[:]) # Assim funciona em listas, o dicionario usa:
    brasil.append(estado.copy()) # Cria cópia de dicionario
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    #Ou somente para values:
    '''
    for v in e.values():
        print(v, end=' ')
    print()
    '''

