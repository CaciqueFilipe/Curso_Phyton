# Váriaveis compostas

**Em Python, existem 3 tipos de váriaveis compostas: tuplas, listas e dicionarios**

## Dicionários

- Diferente das listas, os dicionários consegue personalizar os indices, as diferentes formas de identificação:

```txt
Tuplas - ()
Listas - []
Dicionarios - {}
```

### Iniciando um dicionario

- Posso iniciar usando `dict()` ou `{}`

```py
dados = dict()
dados2 = {}
```

- Já iniciando com índices

```py
dados = { 'nome': 'Pedro', 'idade': 25 }
```

### Exibindo

- Agora ele reconhece pelos indices criados:

```py
print(dados['nome']) # Pedro
print(dados['idade']) # 25
```

### Adicionando novo indice que não existe

- Eu não preciso dar o comando append, ele é exclusivo das listas, nos dicionarios posso gerar direto:

```py
dados['sexo'] = 'M'
```

### Removendo elementos

- Removemos com o comando `del`

```py
del dados['idade']
```

- O Pyhton chamos os elementos de **chaves ou keys**

### Exibindo itens

```py
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

# Retornando valores:
print(filme.values())  #

# Retornando chaves:
print(filme.keys())  #

# Retornando chaves e valores:
print(filme.items())
```

### Usando em laços

```py
for k, v in filme.items():
    print(f'O {k} é {v}')

# O titulo é Star Wars
# O ano é 1977
# O diretor é George Lucas
```

## Podes usar todos os tipos juntos

- Podemos usar Tuplas, Listas e Dicionarios tudo junto. Exemplo:

```py
locadora = [
    {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    },
    {
        'titulo': 'Avengers',
        'ano': 2012,
        'diretor': 'Joss Whedon'
    },
    {
        'titulo': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
    }
]

print(locadora[0]['ano']) # 1977
print(locadora[2]['titulo']) # Matrix
```

