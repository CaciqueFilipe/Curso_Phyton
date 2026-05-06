# Crie um programa que leia um numero inteiro qualquer e mostre na tela se ele é PAR ou IMPAR

from time import sleep
n = int(input("Digite um numero:"))
resto = n% 2
print('{:=^20}'.format('VERIFICANDO SE NUMERO É PAR OU IMPAR...'))
sleep(2)
if resto == 1:
    print("O numero {} é impar". format(n))
else:
    print("O número {} é par". format(n))