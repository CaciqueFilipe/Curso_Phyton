# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exercer 30% do salário ou então o empréstimo será negado.

# Apenas para usar a pasta cores
import sys
import os
from time import sleep
# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

print('{}EMPRESTIMO BANCÁRIO{}'.format(
    cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"],
    cores["limpa"]
))

# valor = float(input('Qual o valor do imóvel?'))
valor = float(input('Qual o valor do imóvel: R$ '))
# salario = float(input('Qual o salário do comprador?'))
salario = float(input('Qual o salário do comprador: R$ '))
# anos = int(input('Quantos anos vai pagar?'))
anos = int(input('Quantos anos de financimento? '))

print('{}{:=^20}{}'.format(
    cores["amarelo"]["amareloNegrito"],
    'VERIFICANDO...',
    cores["limpa"]
))
sleep(2)

prestacao = valor / (anos * 12)
# margem = salario * 0.3
margem = salario * 30 /100 # Mais facil ler

print('{}Pra pagar um casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}{}'.format(
    cores["branco"]["brancoNegrito"],
    valor,
    anos,
    prestacao,
    cores["limpa"]
))

if prestacao > margem:
    print('Seu empréstimo foi {}NEGADO!{}'.format(
        cores['vermelho']['fundoVermelhoTextoBrancoNegrito'],
        cores['limpa']
    ))
else:
    print('Seu empréstimo foi {}APROVADO!{}'.format(
        cores['verde']['fundoVerdeTextoBrancoNegrito'],
        cores['limpa']
    ))