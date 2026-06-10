# Módulos e Pacotes

## Módulos

- A modularização surgiu no ínicio da década de 60

- Sistemas ficando cada vez maiores

- Foco: Dividir um programa grande

- Foco: Aumentar a legibilidade (Encontrar algo em arquivos grandes)

- Foco: Facilitar a manutenção

> Usamos módulos para dividir um problemão em pequenos problemas

### Exemplo de uma modularização

- Se tenho o código:

```py
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
```

- Imagina que o programa começou a ficar grande. Posso pegar o código das funções e criar um novo arquivo uteis.py separado e usar o comando import uteis

```py
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
```

### Vantagens

- Organização do código

- Facilidade na manutenção

- Ocultação de código detalhado

- Reutilização em outros projetos


## Pacotes

- Quando a quantidade de modulos fica muito grande, entra em questão o uso de pacotes (bibliotecas).

> Nada mais é do que uma pasta que contém módulos

- Agora nós temos o pacote uteis com "temas" especificos dentro, exemplo números, datas, strings, cores, etc... e dentro de cada um varias funções.

- Para importar tudo usamos `import uteis`, se quero algo especifico, `from uteis import datas`

> Em python, todo arquivo .py é considerado um módulo e toda pasta considerada um pacote

- Como fica no diretório?

```txt
-uteis
-- cores
--- __init__.py
--- cores.py
--- __init__.py
-- datas
--- __init__.py
-- numeros
--- __init__.py
-- cores
--- __init__.py
```

- Pasta uteis com pastas dentro e cada pasta um arquivo chamado `__init__.py`

### Criando um pacote
