# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente deste ângulo.

import math

angulo = int(input('Digite o valor do angulo:'))
#seno = math.sin(angulo) #coreção abaixo
seno = math.sin(math.radians(angulo))
#cosseno = math.cos(angulo) #coreção abaixo
cosseno = math.cos(math.radians(angulo))
#tangente = math.tan(angulo) #coreção abaixo
tangente = math.tan(math.radians(angulo))

print('O ângulo foi {}, seu Seno é {:.2f}, seu Cosseno é {:.2f}, sua Tangente é {:.2f}'.format(
    angulo,
    seno,
    cosseno,
    tangente
))

'''
## Outra opção sugerida pelo Gustavo:

from math import radians, sin, cos, tan

print("\n{:=^20}".format(" Gustavo "))
angulo = int(input('Digite o valor do angulo:'))
radius = radians(angulo)
seno = sin(radius)
cosseno = cos(radius)
tangente = tan(radius)

print('O ângulo foi {}, seu Seno é {:.2f}, seu Cosseno é {:.2f}, sua Tangente é {:.2f}'.format(
    angulo,
    seno,
    cosseno,
    tangente
))
'''