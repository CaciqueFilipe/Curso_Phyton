# Váriaveis compostas

**Em Python, existem 3 tipos de váriaveis compostas: tuplas, listas e dicionarios**

## Listas

- As listas diferentes das Tuplas, eu consigo modificar seu elementos.

```py
# TUPLAS:
lanche = (hamburguer, suco, pizza, pudim)
print(lanche[2]) # pizza
lanche[3] = 'picole' # Aqui da erro, as tuplas são imutáveis

# LISTAS
lanche = [hamburguer, suco, pizza, pudim]
print(lanche[2]) # pizza
lanche[3] = 'picole'
```

> **OBS. As Tuplas usam _parenteses_ e as Listas usam _colchetes_**

## Adicionando elementos

### append

- O método **append** adiciona um novo item no final da lista

```py
lanche.append('cookie)
```

### insert

- Adiciona um item a lista em determinada posição
- Exemplo, quero um item na posicao 0:

```py
lanche.insert(0, 'cachorro quente')
```

## Removendo elementos

### del

- O comando del permite apagar um especifico ou todos:

```py
del lanche[3] # apaga a pizza
```

### pop

- O comado pop também remove, Normalmente ele é usado para remover o ultimo elemento, mas se passar indice também remove na posição informada:

```py
lanche.pop(3) # apaga a pizza
lanche.pop() # remove o último elemento, cookie
```

### remove

- Outro método de remoção, porém aqui, não informa o índice e sim o valor que quer remover:

```py
lanche.remove('pizza') # apaga a pizza
```

> **OBS. Se tentar remover um indice e ele não existir eu recebo um erro! Mas calma, existem maneiras de ver se o item existe**

- Ex: Aqui a pizza já não existe:
```py
if 'pizza' in lanche: # condição para verificar
    lanche.remove('pizza') # apaga a pizza
```

## Criando listas

### List

- Conseguimos criar uma lista usando a funcao list com range:

```py
valores = list(range(4,11))
# cria uma lista dentro de valores = [4, 5, 6, 7, 8, 9, 10]
```

- Outra forma diretamente com colchetes:

```py
valores = [4, 5, 6, 7, 8, 9, 10]
```

## Ordenação

### sort

- Se quiser ordenar uma lista basta usar o comando sort:
```py
valores = [8, 2, 5, 4, 9, 3 ,0]
valores.sort() # [0, 2, 3, 4, 5, 8, 9]
```

- Caso queira o inverso:
```py
valores.sort(reverse=True) # [9, 8, 5, 4, 3, 2, 0]
```

## Para saber o tamanho da lista

### len

- Verifica o tamanho da lista:
```py
valores = [8, 2, 5, 4, 9, 3 ,0]
len(valores) # 7
```

