# LISTAS
#
# As listas diferentes das tuplas, são mutáveis:
# Agora veremos listas dentro de listas

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste) # ['Gustavo', 40]

print()

'''
galera = []
galera.append(teste)
print(galera) # [['Gustavo', 40]]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera) # [['Maria', 22], ['Maria', 22]]
'''

# Aconteceu pq criou uma ligação, então tenho de fazer copia

galera = []
galera.append(teste[:])
print(galera) # [['Gustavo', 40]]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera) # [['Gustavo', 40], ['Maria', 22]]

print()

# Declarando diretamente:
galera = [['Filipe', 30], ['Heloá', 12], ['Suellen', 34]]
print(galera) # [['Filipe', 30], ['Heloá', 12], ['Suellen', 34]]
print(galera[0]) # ['Filipe', 30]
print(galera[0][0]) # Filipe
print(galera[2][1]) # 34

print()

# Percorrendo a lista:
for p in galera:
    #print completo da pessoa:
    print(p)
    # Só o nome:
    print(f'Nome: {p[0]}')
    #Só a idade:
    print(f'Idade: {p[1]}')
    print()

# Acrescentando via dados digitados:

galera = list()
dado = []
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # copia para galera
    dado.clear() # Limpa a lista para novo dado

print(galera)

print()

# Mostra somente mais de 21 anos
totMai = totMen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totMai += 1
    else: 
        print(f'{p[0]} é menor de idade.')
        totMen += 1
print(f'Temos {totMai} maiores e {totMen} menores de idade.')