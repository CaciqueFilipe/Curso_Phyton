# Condições Aninhadas

- São estruturas de condição dentro de estruturas de condição

> EX:

```
se (condicao)
senao se (outra condicao)
senao
```

- Em Python:

```py
if carro.esquerda():
    bloco True
elif carro.direita():
    bloco True
else:
    bloco True
```

- Esta é a mais simplificada, podem existir mais `elif` quiser desde que comece o primeiro com `if`.