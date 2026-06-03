# Váriaveis compostas

**Em Python, existem 3 tipos de váriaveis compostas: tuplas, listas e dicionarios**

## Listas - Parte 2

- **Aqui veremos listas dentro de listas - Listas compostas**

```py
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) # Pedro
print(dados[1]) # 25
```

- Agora vamos colocar listas dentro das outras:

```py
pessoas = list()
pessoas.append(dados[:]) # Pega copia de tudo da outra lista

# Colocando mais pessoas na lista:
dados2 = list()
dados2.append('Maria')
dados2.append(19)
pessoas.append(dados2[:])
```

- Como declarar tudo de uma vez?

```py
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
```

- Como exibir dados agora?

```py
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]
```



