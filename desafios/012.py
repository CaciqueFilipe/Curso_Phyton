# Crie um programa que leia o preço de um produto e mostre seu preço com 5% de desconto.

preco = float(input("Qual o preço do produto?"))
desconto = preco - (preco * 5 / 100)
input('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))