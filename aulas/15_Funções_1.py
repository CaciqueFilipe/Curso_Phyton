# Exemplo de rotina que pode virar função:
'''
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

'''
# Transformando em função:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4,5)
soma(8,9)
soma(2,1)
#soma(4) # ERROO, precisa de dois parametros
soma(a=4, b=5) # Posso especificar o parametro
soma(b=4, a=5) # Outra inversa
#soma(b=4, 5) # ERROO, ele não sabe que o outro é a, precisa especificar
#soma(3,9,5) # ERROO, passando mais parametros que o necessário

print()
print()


## Empacotador de parametros
def contador(*núm): # o * indica vários do empacotador
    #print(núm) # retorna uma tupla
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
    # Mostrando tamanho
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


# Mesma função com quantidade diferentes de parametros
contador(5,7,3,1,4)
print()
contador(8,4,7)

print()
print()


## Trabalhando com listas

# exemplo, se eu precisasse dobrar valores de uma lista?
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)

print()
print()

# pegando primeiro exemplo de soma usando empacotador, com varios parametros:
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4)