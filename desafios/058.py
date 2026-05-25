# Melhore o jogo do desafio 028 onde o computador "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
'''
from random import randint
from time import sleep

computador = randint(0,5) # Faz o computador "PENSAR"
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

palpites = 0
jogador = 0
while jogador != computador:
    texto = "Em que numero eu pensei?" if jogador == 0 else "Não foi esse, tente outro: "
    jogador = int(input("{}".format(texto))) # Jogador tenta adivinhar
    print('PROCESSANDO...')
    sleep(3)
    palpites += 1
print('PARABÉNS! Você conseguiu me vencer após {} palpites!'.format(palpites))
'''

# Pelo Gustavo
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
