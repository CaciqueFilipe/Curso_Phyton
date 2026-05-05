# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente deste ângulo.

import math

angulo = int(input('Digite o valor do angulo:'))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O ângulo foi {}, seu Seno é {:.2f}, seu Cosseno é {:.2f}, sua Tangente é {:.2f},'.format(
    angulo,
    seno,
    cosseno,
    tangente
))