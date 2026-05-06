# Escreva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Consigo formar um triangulo')
else:
    print('Não dá para formar um triangulo')

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20))
r1 = float(input("Primeiro segmento:"))
r2 = float(input("Segundo segmento:"))
r3 = float(input("Terceiro segmento:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")
'''

