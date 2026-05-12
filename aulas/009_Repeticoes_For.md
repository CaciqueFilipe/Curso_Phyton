# Estrutura de Controle - Repetição

- Pode chamar de iteração ou laço de repetição

## Estruturas For - simples

- Ex: Temos um jogador e ele precisa dar 5 ou mais passos até chegar a maça

```txt
laço c no intervalo(1,10):
    passo
pega
```

- Em Python

```py
for c in range(1,10):
    passo
pega
```

- E se eu quiser dar dois passos e pular?

```txt
laço c no intervalo(0,3):
    passo
    pula
passo
pega
```

- Em Python

```py
for c in range(0,3):
    passo
    pula
passo
pega
```

## Utilizando uma estrutura de controle dentro do for

- E se agora tiver moedas no meio do caminho e eu quiser pegar

```txt
laço c no intervalo(0,3):
    se moeda
        pega
    passo
    pula
passo
pega
```

- Em Python

```py
for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega
```


