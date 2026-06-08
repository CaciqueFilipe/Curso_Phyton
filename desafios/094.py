# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista
# No final, mostre:
#
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

pessoas = []
pessoa = {}
totIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True: # Validação de entrada, campo sexo:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    totIdade += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True: # Validação de quer continuar:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
qtd_pessoas = len(pessoas)
media = totIdade / qtd_pessoas
print(f'- O grupo tem {qtd_pessoas} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p['nome']}', end=' ')
print()
print('- Lista das pessoas acima da média:')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
    print()
print('<< ENCERRADO >>')