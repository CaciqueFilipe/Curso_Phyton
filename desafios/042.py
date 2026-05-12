# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

fundoAmareloTextoVermelhoNegrito = cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"]
verdeNegrito = cores["verde"]["verdeNegrito"]
noColor = cores["limpa"]

print("-=-" * 20)

print('{}ANALISADOR DE TRIÂNGULOS{}'.format(
    fundoAmareloTextoVermelhoNegrito,
    noColor
))

print("-=-" * 20)
r1 = float(input("Primeiro segmento:"))
r2 = float(input("Segundo segmento:"))
r3 = float(input("Terceiro segmento:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo ", end='')
    if r1 == r2 == r3:
        print("{}EQUILATERO!{}".format(
            verdeNegrito,
            noColor
        ))
    elif r1 != r2 != r3 != r1:
        print("{}ESCALENO!{}".format(
            verdeNegrito,
            noColor
        ))
    else:
        print("{}ISÓSCELES!{}".format(
            verdeNegrito,
            noColor
        ))
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")
