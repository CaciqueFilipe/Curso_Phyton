# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas valores pares e os valores impares digitados, respectivamente
# Ao final, mostre o conteudo das 3 listas

valores = []
pares = []
impares = []

resp = 'S'
while resp in 'S':
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('-=' *30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
