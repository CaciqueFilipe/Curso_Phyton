# Manipulando textos em Python

## O que é cadeia de caracteres ou string

- Tudo que esta entre aspas simples ou duplas são strings
>Ex: 'Curso em Video Python'

- Ao alocar esta frase em uma variavel, ele armazena na memoria
> Ex: `frase = 'Curso em Video Python'`

- Foi alocada uma string com 20 posições.

## Fatiamento

- Se eu escrever no python `frase[9]` ele traz o decimo caractere 'V'.
> Nota: para o python V maiusculo e v minusculo são diferentes

- Outro exemplo `frase[9:13]` ele traz os caracteres 'Vide'.
> Nota: se quiser a palavra teria que ser 9:14, um a mais no final

- E agora se quiser `frase[9:21]` será que da erro sendo que tenho 20 caracteres?
> Nota: Neste caso ele vai trazer 'Video Python' por parar no 20, mas para saber o fim esta não é a melhor solução, tem outras melhores

- Também é possivel fazer `frase[9:21:2]`, seria começa no 9, termina no 21 e pula de 2 em 2.
> Nota: 'VdoPto'

- Outra maneira `frase[:5]`, omitindo o valor antes dos dois pontos ele começa do inicio.
> Nota: 'Curso'

- Outra forma `frase[15:]`, omitindo após os dois pontos ele trará até o final.
> Nota: 'Python'

- Outra maneira `frase[9::3]`, começa em 9 até o final pulando de 3 em 3.
> Nota: 'VePh'

## Função len

- *len* Vem de length que quer dizer comprimento.

- Ex: `len(frase)`, ele trara a quantidade de caracteres de frase. `21 caracteres`

## Função count

- Semelhante ao len, ele conta algo na frase

- Com o *count* seria:

- Ex: `frase.count('o')`, ele trara a quantidade de caractere 'o' na frase. `3 caracteres`

- Outra opção de uso do count:

- Ex: `frase.count('o', 0, 13)`, ele trara a quantidade de caractere 'o' na frase começando no 0 até a 13ª posição (sem ela). `1 caracteres`

## Função find

- Procura algo na string

- Ex: `frase.find('deo')`, ele trará a posição se encontrar a palavra. `11`
- Se procurar `frase.find('android')`, ele irá retornar `-1` pois não encontrou.

## Operador in

- Semelhante ao find, porém retorna True ou False
- Ex: `'Curso' in frase`, ele retornará `True`

## Transformação

### Replace

- Substitui algo no texto
- Ex: `frase.replace('Python', 'Android')`, troca na frase 'Python' por 'Android'.

### Upper

- Pra cima, tranforma em maiusculas
- Ex: `frase.upper()`, vai tornar tudo em maiusculo

### Lower

- Pra baixo, tranforma em minusculas
- Ex: `frase.lower()`, vai tornar tudo em minusculo

### Capitalize

- Deixa somente o primeiro caractere em maiusculo
- Ex: `frase.capitalize()`, vai tornar o primeiro caractere em maiusculo 

### Title

- Deixa o primeiro caractere de cada palavra em maiusculo
- Ex: `frase.title()`, vai tornar o primeiro caractere de cada palavra em maiusculo

### Strip

- Remove espaços do começo da string:
```py
frase = '   Aprendendo Python  '
frase.strip()
print(frase)
# Saida 'Aprendendo Python'
```

### RStrip

- R de Right, existem em muitas funções
- Remove espaços do final da string:
```py
frase = '   Aprendendo Python  '
frase.rstrip()
print(frase)
# Saida '   Aprendendo Python'
```

### LStrip

- L de Left
- Remove espaços da esquerda da string:
```py
frase = '   Aprendendo Python  '
frase.lstrip()
print(frase)
# Saida 'Aprendendo Python  '
```

## Divisão

### Split

- `frase.split()` Dividi a string considerando por padrão os espaços e forma uma lista de palavras:

### Juncao

- `'-'.join(frase)`, após split posso juntar em uma string com traços entre elas, se quiser espaço basta colcar `' '.join(frase)`


