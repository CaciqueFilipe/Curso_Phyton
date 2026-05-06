# Escreva um programa que leia a velocidade do carro.
# Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

from time import sleep
velocidade = int(input("Qual a velocidade do veículo?"))
print('{:=^20}'.format('VERIFICANDO RADAR...'))
sleep(3)
if velocidade > 80:
    print("Você foi multado!")
    print("A velocidade máxima é de 80km/h e voce estava a {}km/h".format(velocidade))
    print('{:=^20}'.format('VERIFICANDO VALOR DA MULTA...'))
    sleep(3)
    multa = (velocidade - 80) * 7
    print("Sua multa é de R${:.2f}".format(multa).replace('.', ','))
else:
    print("Velocidade abaixo do limite do radar, boa viagem!")
