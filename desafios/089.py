# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
notas = []
while True:
    nome = str(input('Nome: '))
    for c in range(0,2):
        notas.append(float(input(f'Nota {c}: ')))
    alunos.append([nome, notas[:]])
    notas.clear()
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'N':
        break
print('-='*30)
print('Nº   NOME    MÉDIA')
print('-'*15)
for num, aluno in enumerate(alunos):
    soma = 0
    print(f'{num}   {aluno[0]}  ', end='')
    for nota in aluno[1]:
        soma += nota
    media = soma / 2
    print(f'{media:.2f}')
print('-'*15)

while True:
    opcao = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if 0 <= opcao < len(alunos):
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
        print('-'*15)
    else:
        print('Opção inválida! tente novamente.')
print('FINALIZANDO...')
print('-='*4, end='')
print(' < VOLTE SEMPRE > ', end='')
print('-='*4)