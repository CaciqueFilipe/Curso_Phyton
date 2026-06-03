# Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única
# que mantenha os valores pares e impares. No final mostre os valores pares e ímpares em ordem crescente.

#pares 0 e impares 1
valores = [[], []]

for c in range(0,7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

print('-=' * 30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

