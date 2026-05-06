# Escreva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))

if (a + b) > c:
    if (a + c) > b:
        if (b + c) > a:
            print('Consigo formar um triangulo')
        else:
            print('Não dá para formar um triangulo')

