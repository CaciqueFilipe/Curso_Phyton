# Interactive Help

## Usando help
help(print)

## Usando doc
print(input.__doc__)

# docstrings

def contador(i,f,p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: ínicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2,10,2)
help(contador)

# Argumentos opcionais

def somar(a = 0, b = 0, c = 0): # Aqui ao atribuir valor, ele deixa opcional
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2,5) # 10
somar(8,4) # 12
somar() # 0
somar(b=4, c=2) # 6


## Escopo de variáveis

def teste():
    x = 8 # Escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2 # Escopo global
print(f'No programa principal, n vale {n}')
teste()
# print(f'Na programa principal, x vale {x}') # ERRO! x tem escopo local apenas no teste


### Para mudarmos temos de usar a palavra **global**, exemplo:

def funcao():
    global n1 # Palavra reservada para alterar variavel global
    n1 = 4
    print(f'N1 dentro vale {n1}')


# Programa Principal
n1 = 2 # Escopo global
funcao()
print(f'N1 fora vale {n}')

# Saída
# N1 dentro vale 8
# N1 fora vale 8


# Retorno de resultados

### As funções podem ou não retornar algo, se quisermos retornar usamos a palavra **return**. Exemplo:

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s # Aqui retorna valor


r1 = somar(3,2,5)
r2= somar(1,7)
r3= somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

