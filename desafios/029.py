# Escreva um programa que leia a velocidade do carro.
# Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

import sys
import os
from time import sleep

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

velocidade = int(input("Qual a velocidade do veículo?"))
print('{}{:=^20}{}'.format(
    cores["azul"]["fundoAzulTextoBranco"],
    'VERIFICANDO RADAR...',
    cores["limpa"]
))
sleep(3)
if velocidade > 80:
    print("{}Você foi multado!{}".format(
        cores["vermelho"]["vermelhoNegrito"],
        cores["limpa"]
    ))
    print("{}A velocidade máxima é de 80km/h e voce estava a {}km/h{}".format(
        cores["amarelo"]["amareloNegrito"],
        velocidade,
        cores["limpa"]
    ))
    print('{}{:=^20}{}'.format(
        cores["vermelho"]["fundoVermelhoTextoAmarelo"],
        'VERIFICANDO VALOR DA MULTA...',
        cores["limpa"]
    ))
    sleep(3)
    multa = (velocidade - 80) * 7
    print("{}Sua multa é de R${:.2f}{}".format(
        cores["vermelho"]["vermelhoNegrito"],
        multa,
        cores["limpa"]
    ).replace('.', ','))
else:
    print("{}Velocidade abaixo do limite do radar, boa viagem!{}".format(
        cores["verde"]["verdeNegrito"],
        cores["limpa"]
    ))

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
velocidade = int(input("Qual a velocidade do veículo atual do carro?"))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    multa = (velocidade - 80) * 7
    print('Vocẽ deve pagar uma multa de R${:.2f}'.format(multa).replace('.', ',')
print("Tenha um bom dia! Dirija com segurança!")
'''
