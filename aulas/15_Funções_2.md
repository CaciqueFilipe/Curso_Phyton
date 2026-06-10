# Funções (def) - Parte 2

- Vamos ver aqui o que são Interactive Help, docstrings, Argumentos opcionais, Escopo de variáveis e Retorno de resultados

## Interactive Help

- Ajuda interativa (), para usar basta usar a função **help()**.

- Ex no python console:

```py
help()
# depois buscar o que quer ver na documentação
print
# Analisar
# Para sair
quit
```

- Ex no arquivo pyhton:

```py
help(print)
```

- Outra forma é usando o comando com **doc**.

- Ex:
```py
print(input.__doc__)
```

## docstrings

- Toda função tem sua documentação, vimos com o uso do **help** e **__doc__**. Mas e as funções que nós criamos? Como documentar? Ai vem as docstrings.

```py
def contador(i,f,p):
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2,10,2)
help(contador) #?
```

- Para declarar uma docstring voce coloca 3 aspas duplas abrindo e 3 fechando apos a declaração, Ex:

```py
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
help(contador) #?
```

## Argumentos opcionais

- As vezes nossa função precisa de argumentos opcionais. Exemplo e se nossa função somar precisasse de 3 parametros mas um deles fosse opcional?

```py
def somar(a = 0, b = 0, c = 0): # Aqui ao atribuir valor, ele deixa opcional
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2,5)
somar(8,4) # Aqui vai funcionar normalmente
somar() # Pega todos opcionais
```

## Escopo de variáveis

- Basicamente significa o local onde minha variável vai existir, exemplo:

```py
def teste():
    print(f'Na função teste, n vale {n}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
```

> Neste exemplo, n tem escopo global e pode ser usado na função teste.

- Outro exemplo mostrando escopo local:

```py
def teste():
    x = 8 # Escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2 # Escopo global
print(f'No programa principal, n vale {n}')
teste()
# print(f'Na programa principal, x vale {x}') # ERRO! x tem escopo local apenas no teste
```

- Em Python não modificamos variaveis globais dentro de função desta forma, exemplo:

```py
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


# Programa Principal
n1 = 2 # Escopo global
funcao()
print(f'N1 fora vale {n}')

# Saída
# N1 dentro vale 4
# N1 fora vale 2
```

- Para mudarmos temos de usar a palavra **global**, exemplo:

```py
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
```

> Também temos importação local e importação global

## Retorno de resultados

- As funções podem ou não retornar algo, se quisermos retornar usamos a palavra **return**. Exemplo:

```py
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s # Aqui retorna valor


r1 = somar(3,2,5)
r2= somar(1,7)
r3= somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
```


