# Interrompendo Estrutura de Repetição - While com Break

- Semelhante a aula anterior, tenho a seguinte situação:

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

- E se no meio do caminho tiver um trofeu e quando ele pegar o jogo acaba?

```txt
enquanto verdadeiro
    se chão
        passo
    se buraco
        pula
    se moeda
        pega
    se trofeu
        pula
        interrompa
pega
```

```py
while True:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if troféu:
        pula
        break
pega
```

## Nova maneira de digitar strings = fstrings
```py
s = 5
print(f'A soma vale {s}')
```