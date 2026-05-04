# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerar 1 dólar = 3.27

dolar = 3.27
n = float(input("Quanto dinheiro você tem na carteira?"))
conversao = n / dolar
print("Com R${:.2f} você pode comprar US${:.2f}.".format(n, conversao))