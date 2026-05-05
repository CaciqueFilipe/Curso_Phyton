# Operadores Aritmeticos

## Quais são os operadores

- Existem 7 operadores:

- Soma (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Potenciação (**)
- Divisão inteira (//)
- Resto da divisão (%)

Ex:

| Operação | Operador | Expressão | Resultado |
| :--- | :---: | :---: | :---: |
| Soma | + | 5 + 2 | 7 |
| Subtração | - | 5 - 2 | 3 |
| Multiplicação | * | 5 * 2 | 10 |
| Divisão | / | 5 / 2 | 2.5 |
| Potenciação | ** | 5 ** 2 | 25 |
| Divisão Inteira | // | 5 // 2 | 2 |
| Resto da Divisão | % | 5 % 2 | 1 |

## Ordem de precedencia

1. `()`  - parenteses
2. `**` - exponenciação
3. `* / // %` - multiplicação, divisão, divisão inteira, resto da divisão (O que aparecer primeiro)
4. `+ -` - adição e subtração


Ex:
```py
- 5 + 3 * 2 == 11
- 3 * 5 + 4 ** 2 == 31
- 3 * (5 + 4) ** 2 == 243

# Mais exemplos:
5**2 == 25
19//2 == 9
19/2 == 9.5
365**522 == #(numero gigante aqui, isso faz o python util para grandes calculos)
18%2 == 0
122%3 == 2
4**3 == 64
pow(4, 3) == 64 #(Aqui perde a precedencia pois é uma função)
81**(1/2) == 9.0 # Raiz quadrada de 81
25**(1/2) == 5.0 # Raiz quadrada de 25
127**(1/3) == 5.026525... # Raiz cubica de 127
```

