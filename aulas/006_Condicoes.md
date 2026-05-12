# Condições Simples e Compostas

### Condição if else

- if (Se), else (Senão) - se a estrutura tiver apenas if, ela é simples, se for if e else, ela é composta
```
Se (condição verdadeira)
    executa bloca
Senao
    executa outro bloco
```

- Ex:

```py
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
```
> Nota: A identação é importante, todo comando a esquerda é executado sempre o bloco identado depende da condição

- Outra forma usando condição simplificada

```py
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')
```

