# Crie um programa que leia um numero inteiro qualquer e mostre na tela se ele é PAR ou IMPAR
import sys
import os
from time import sleep

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

n = int(input("{}Digite um numero:{}".format(
    cores["roxo"]["roxoNegrito"],
    cores["limpa"]
)))
resto = n% 2
print('{}{:=^20}{}'.format(
    cores["azul"]["fundoAzulTextoBranco"],
    'VERIFICANDO SE NUMERO É PAR OU IMPAR...',
    cores["limpa"]
))
sleep(2)
if resto == 1:
    print("{}O numero {} é impar{}".format(
        cores["vermelho"]["vermelhoNegrito"],
        n,
        cores["limpa"]
    ))
else:
    print("{}O número {} é par{}".format(
        cores["verde"]["verdeNegrito"],
        n,
        cores["limpa"]
    ))

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
número = int(input("Me diga um número qualquer:"))
resultado = número % 2
if resultado == 0:
    print("O número {} é PAR".format(número))
else:
    print("O número {} é ÍMPAR".format(número))
'''
