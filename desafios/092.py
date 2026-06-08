# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario
# Se por acaso CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoas vai se aposentar.
# Considerar aposentadoria com 35 anos de colaboração

from datetime import datetime

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.now().year

pessoa['idade'] = ano_atual - ano_nascimento
pessoa['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['cpts'] != 0:
    pessoa['contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - ano_atual)

print('-=' * 30)
# print(pessoa)
for k,v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
