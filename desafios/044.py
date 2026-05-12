# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

fundoAmareloTextoVermelhoNegrito = cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"]
azulNegrito = cores["azul"]["azulNegrito"]
vermelhoNegrito = cores["vermelho"]["vermelhoNegrito"]
amareloNegrito = cores["amarelo"]["amareloNegrito"]
verdeNegrito = cores["verde"]["verdeNegrito"]
noColor = cores["limpa"]

print("-=-" * 20)

print('{}VALOR A PAGAR NO PRODUTO{}'.format(
    fundoAmareloTextoVermelhoNegrito,
    noColor
))
print("-=-" * 20)

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X cartão
[ 4 ] 3X ou mais cartão
'''
)

opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('{}Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS{}'.format(
        azulNegrito,
        parcela,
        noColor
    ))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input('Quantas parcelas?'))
    parcela = total / totalParcelas
    print('{}Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS{}'.format(
        azulNegrito,
        totalParcelas,
        parcela,
        noColor
    ))
else:
    total = preco
    print('{}OPÇÃO INVÁLIDA de pagamento, Tente novamente!{}'.format(
        vermelhoNegrito,
        noColor
    ))
print("{}Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.{}".format(
        amareloNegrito,
        preco,
        total,
        noColor
    ))