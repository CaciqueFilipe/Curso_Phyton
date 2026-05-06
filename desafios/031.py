# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

from time import sleep

distancia = int(input("Digite a distância da viagem em Km:"))
print('{:=^20}'.format('CALCULANDO PASSAGEM...'))
sleep(2)

if distancia <= 200:
    passagem = distancia * 0.5
    print("A passagem custa R${:.2f}".format(passagem).replace(".", ","))
else:
    passagem = distancia * 0.45
    print("A passagem custa R${:.2f}".format(passagem).replace(".", ","))