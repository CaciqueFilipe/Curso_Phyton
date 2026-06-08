# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno["Nome"] = str(input('Nome: '))
aluno["Média"] = float(input('Média: '))

if 7 > aluno["Média"] >= 5:
    aluno["Situação"] = "RECUPERAÇÃO"
elif aluno["Média"] < 5:
    aluno["Situação"] = "REPROVADO"
else:
    aluno["Situação"] = "APROVADO"

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

