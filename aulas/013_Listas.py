# LISTAS
#
# As listas diferentes das tuplas, são mutáveis:
num = [2, 5, 9, 1]
num[2] = 3
print('Lista inicial: ', num) # [2, 5, 3, 1]

# Se tentar adicionar assim da ERRO, pois o indice não existe
# num[4] = 7 # ERROOOO

# Adicionamos assim:
num.append(7)
print('Novo num com 7 no final: ', num)

# Posso sortear:
num.sort()
print('Sorteado: ', num)
# Se quiser sortear inverso:
num.sort(reverse=True)
print('Sorteado reverso: ', num)

print(f'Esta lista tem {len(num)} elementos.')

# Adicionando novos valores
num.insert(2, 0) # 0 na posição 2
print(f'Com 0 na 2ª posição: {num}')

# Removendo elementos
num.pop() #Remove o ultimo elemento
print(f'Removi último elemento com pop: {num}')

# Removendo um index especifico
num.pop(2)
print(f'Removi index da 2ª posição: {num}')

# Outras remoções:
num.insert(2,2) #Inseri um novo elemento para comportamento:
print(f'Adicionei 2 na 2ª posição: {num}')

# removendo por busca, será que remove todos os numeros 2?
num.remove(2)
print(f'Removi o número 2: {num}')
# Remove apenas o primeiro que encontrar! Da para remover todos usando laços

# Se tentar remover algo que não esta na lista da erro:
#num.remove(4) #ERROOOO
# usando if
if 4 in num:
    num.remove(4) 
else:
    print('Não achei o número 4')

print('-=' * 30)
## Iniciando uma nova lista
valores = [] # ou valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

#print(valores) # de forma mais bonita:
for valor in valores:
    print(f'{valor}...', end='')
print()

valores = list()


# Adicionando valores digitados pelo usuario:
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print()

# Se quiser o indice também:
for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}!')
print('Cheguei ao final da lista')

print('-=' * 30)

# Peculiaridades no Python:
a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# O PYTHON CRIA UMA LIGAÇÃO DAS LISTAS E SE ALTERA UMA ELE MUDA NA OUTRA!!!
# Para copiar:
a = [6,5,9,7]
b = a[:] # linha que cria copia de lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('-=' * 30)