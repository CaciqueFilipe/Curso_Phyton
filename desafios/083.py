# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []
for sím in expr:
    if sím == '(':
        pilha.append('(')
    elif sím == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

