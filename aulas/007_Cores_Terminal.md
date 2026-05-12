# Para mudar a cor do terminal usamos um comando

- Código ansi para cores: `\033[0;33;44m`
> Nota: os valores após o colchete são style; text; back

## Codigos para estilo

```
0 - none
1 - bold
4 - underline
7 - negative
```

## Codigos para texto

```
- 30 - branco
- 31 - vermelho
- 32 - verde
- 33 - amarelo
- 34 - azul
- 35 - roxo
- 36 - azul claro
- 37 - cinza
```

## Codigos para fundo

```
- 40 - branco
- 41 - vermelho
- 42 - verde
- 43 - amarelo
- 44 - azul
- 45 - roxo
- 46 - azul claro
- 47 - cinza
```

## Exemplos

- Escrever a palavra "Teste" com fundo vermelho e letra branca:
`\033[0;30;41m`

- Escrever a palavra "Teste" sublinhado com fundo azul e letra amarela:
`\033[4;33;44m`

- Escrever a palavra "Teste" negrito com fundo amarelo e letra roxa:
`\033[1;35;43m`

- Escrever a palavra "Teste" com fundo preto e letra branca:
`\033[m`

- Escrever a palavra "Teste" negrito com fundo branco e letra preta:
`\033[7;30m`
