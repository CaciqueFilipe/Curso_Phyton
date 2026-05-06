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

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
distancia = float(input("Qual a distância da sua viagem?"))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(passagem).replace(".", ","))

## Outra maneira com condição inline:
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preco).replace(".", ","))
'''
