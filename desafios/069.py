# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não continuar.
# No final, mostre:
#
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

maior18 = totMulher20 = totHomem = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        totHomem += 1
    if sexo in 'Ff' and idade > 20:
        totMulher20 += 1

    print('-' * 20)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar in 'Nn':
        break
print('=' * 4, " FIM DO PROGRAMA ", '=' * 4)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {totHomem} homens cadastrados')
print(f'E temos {totMulher20} mulheres com menos de 20 anos.')