# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Primeiro numero:'))
n2 = float(input('Segundo numero:'))
n3 = float(input('Terceiro numero:'))

if n1 > n2 and n1 > n3:
    print("O maior valor é {}".format(n1))
if n2 > n1 and n2 > n3:
    print("O maior valor é {}".format(n2))
if n3 > n1 and n3 > n2:
    print("O maior valor é {}".format(n3))

if n1 < n2 and n1 < n3:
    print("O menor valor é {}".format(n1))
if n2 < n1 and n2 < n3:
    print("O menor valor é {}".format(n2))
if n3 < n1 and n3 < n2:
    print("O menor valor é {}".format(n3))

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
a = int(input("Primeiro valor:"))
b = int(input("Segundo valor:"))
c = int(input("Terceiro valor:"))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))    
'''
