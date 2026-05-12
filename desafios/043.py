# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o IMC e mostre o seu status.
# De acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

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

print('{}ANALISADOR DE IMC{}'.format(
    fundoAmareloTextoVermelhoNegrito,
    noColor
))
print("-=-" * 20)
peso = float(input("Qual é seu peso? (Kg)"))
altura = float(input("Qual é sua altura? (m)"))

imc  = peso / (altura ** 2)
print("{}O IMC desta pessoa é de {:.1f}{}".format(
    azulNegrito,
    imc,
    noColor
))

if imc < 18.5:
    print("{}Você está ABAIXO DO PESO normal{}".format(
        amareloNegrito,
        noColor
    ))
elif 18.5 <= imc < 25:
    print("{}Você está na faixa de PESO NORMAL{}".format(
        amareloNegrito,
        noColor
    ))
elif 25 <= imc < 30:
    print("{}Você está em SOBREPESO{}".format(
        amareloNegrito,
        noColor
    ))
elif 30 <= imc < 40:
    print("{}Você está em OBESIDADE!{}".format(
        amareloNegrito,
        noColor
    ))
elif imc >= 40:
    print("{}Você está em OBESIDADE MÓRBIDA, cuidado!{}".format(
        amareloNegrito,
        noColor
    ))
