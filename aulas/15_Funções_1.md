# Funções (def) - Parte 1

- Funções são usadas para criar e facilitar **ROTINAS**

- Exemplo de funções que já usamos até aqui sem perceber:

```py
print()
len()
input()
int()
float()
```

## Criando uma nova função

- Como usamos muito as definições de linhas, vamos ciar uma função (ROTINA) para isso

```txt
----------------------------
    SISTEMA DE ALUNOS
----------------------------
```

- Eu repito muito as linhas em comandos prints.

```py
def mostraLinha():
    print('----------------------------')
```

- A cada vez que precisar posso mostrar:

```py
mostraLinha()
print('SISTEMA DE ALUNOS')
mostraLinha()
```

> Tem que existir dua linhas vazias após a declaração de função até o programa principal, ex:

```py
def lin():
    print('-' * 30)


# Programa Principal
lin()
print('     CURSO EM VIDEO     ')
lin()
```

## Trabalhando com parametros

- Nós podemos trabalhar com parametros, e passar para as funções

```py
# Facilitando mostrar titulos:
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#Programa Principal
titulo('  CURSO EM VIDEO  ')
titulo('  APRENDA PYTHON ')
```

## Empacotador de parametros

- Exemplo eu tenha uma função contador, e eu possa passar mais parametros que o definido na função, isso o Python permite. Ex:

```py
def contador(*núm): # o * indica vários do empacotador
    

# Mesma função com quantidade diferentes de parametros
contador(5,7,3,1,4)
contador(8,4,7)
```
