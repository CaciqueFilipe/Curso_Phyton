# Váriaveis compostas

**Em Python, existem 3 tipos de váriaveis compostas: tuplas, listas e dicionarios**

## Tuplas

- Se ao inves de eu querer armazenar uma variavel simples, eu gostaria de armazenar uma composta

```txt
// neste caso ele substitui por ser uma variavel simples:
lanche = hamburguer
lanche = suco

// usando uma variavel composta, neste caso a tupla:
lanche = (hamburguer, suco, pizza, pudim)
```

## Tipos de fatiamento

```py
lanche = (hamburguer, suco, pizza, pudim)

print(lanche[2]) # apenas o item da posição 2 - pizza
print(lanche[0:2]) # apenas os itens do começo até a posição 2 - hamburguer, suco, pizza
print(lanche[1:]) # começa da posição 1 até o final - suco, pizza, pudim
print(lanche[-1]) # apenas o último elemento - pudim
print(lanche[-2]) # apenas o penúltimo elemento - pizza
```

## Método len

- Referente ao tamanho

```py
lanche = (hamburguer, suco, pizza, pudim)

print(len(lanche)) # 4
```

## Para estrutura de repetição

```py
lanche = (hamburguer, suco, pizza, pudim)

for c in lanche:
    print(c)
```

> As tuplas são IMUTÁVEIS durante execução do programa
> Se eu defini a variavel lanche daquele jeito, eu não consigo trocar por exemplo um pudim por sorvete
