# Faça um programa que leia um numero e mostre seu dobro, seu triplo e raiz quadrada

n = int(input("Digite um número:"))
dobro = n * 2
triplo = n * 3
raizQuadrada = n ** (1/2)

print("Analisando o valor {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.".format(n, dobro, triplo, raizQuadrada))