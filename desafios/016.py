# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6.

from math import trunc

real = float(input("Digite um numero: "))
print("O numero {} tem a parte inteira {}.".format(real, trunc(real)))
