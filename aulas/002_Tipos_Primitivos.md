# Tipos Primitivos

## Existem varios, por enquanto focamos nestes

- int
- float
- bool
- str

## Int

- Usado para numeros inteiros como 7, -4, 0, 9875 ...

- Ex:
```py
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma vale', s)
```

Outra forma mais moderna:

```py
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))')
```

## Float

- Usado para numeros reais como 4.5, 0.076, -15.223 ...

- Ex:
```py
n1 = float(input('Digite um numero decimal '))
print(type(n1))
```

## Bool

- Usado para valores booleanos sendo True ou False.

- Ex:
```py
n1 = bool(input('Digite algo pra ver se é True ou False'))
print(type(n1))
```

## Str

- Usado para strings como 'Olá', '7.5' ...

- Ex:
```py
n1 = input('Digite algo')
print(type(n1))
```

### Alguns exemplos de possibilidades de operadores aritmeticos com string:

```py
'Oi' + 'Olá' == 'OiOlá'
'Oi' * 5 == 'OiOiOiOiOi'
'=' * 20 == '==================='
print('='*20) # saída: ===================
```

- Usando format

```py
nome = input('Qual é o seu nome? ')
# saída com 20 espaços após nome
print('Prazer em te conhecer {:20}!'.format(nome))
# saída com 20 espaços antes do nome
print('Prazer em te conhecer {:>20}!'.format(nome))
# saída com 20 espaços depois do nome
print('Prazer em te conhecer {:<20}!'.format(nome))
# saída com 20 espaços e nome centralizado neles
print('Prazer em te conhecer {:^20}!'.format(nome))
# saída com 20 iguais e nome centralizado neles
print('Prazer em te conhecer {:=^20}!'.format(nome))
```

- Outras opções

```py
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
```

> não quebra linha no print usar `end=''`, ex: `print('', end=" ")`
> para quebrar usar `\n`, ex: `print('Aqui \n quebrou')`
