# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

# Apenas para usar a pasta cores
import sys
import os
from time import sleep
# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

print('{}COMPARANDO NUMEROS{}'.format(
    cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"],
    cores["limpa"]
))

n1 = int(input('{}Digite o primeiro número:{}'.format(
    cores["vermelho"]['vermelhoNegrito'],
    cores["limpa"]
)))
n2 = int(input('{}Digite o primeiro número:{}'.format(
    cores["verde"]['verdeNegrito'],
    cores["limpa"]
)))

print('{}{:=^20}{}'.format(
    cores["amarelo"]["amareloNegrito"],
    'VERIFICANDO...',
    cores["limpa"]
))
sleep(2)

if n1 > n2:
    print('O {}primeiro valor{} é maior'.format(
        cores["vermelho"]['vermelhoNegrito'],
        cores["limpa"]
    ))
elif n2 > n1:
    print('O {}segundo valor{} é maior'.format(
        cores["verde"]['verdeNegrito'],
        cores["limpa"]
    ))
else:
    print('{}Os valores são iguais!{}'.format(
        cores["amarelo"]['amareloNegrito'],
        cores["limpa"]
    ))