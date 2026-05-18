# Estrutura de Repetição - While

- Outra opção além da estrutura FOR, temos o While, que é a estrutura de repetição com teste lógico.

- Com a mesma situação do jogador que tem que pegar a maça, para explicar a diferença dos dois, e se não soubermos a quantidade de passos? Ai entra o while.

- Se não sei o limite, a estrutura FOR não será possivel, ai temos a estrutura WHILE


- Poderia dizer, Enquanto não chegar na maçã, de passos.

```txt
enquanto não maça
    passo
pega
```

- Em Python:

```py
while not maça:
    passo
pega
```

- E se tivessemos coisas irregulares ate pegar a maça, ai o while consegue atender melhor:


```txt
enquanto não maça
    se chão
        passo
    se buraco
        pula
    se moeda
        pega
pega
```

```py
while not maça:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega
```
