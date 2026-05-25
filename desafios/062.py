# Melhore o desafio 061, perguntando para o usuário se ele que mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print("=" * 20)
print('GERADOR DE PA')
print("=" * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} '.format(termo), end='-> ')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progessão finalizada com {} termos mostrados.'.format(total))
