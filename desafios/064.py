# Crie um programa que leia vários numeros inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999,
# Que é a condição de parada. No final. mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag)

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = int(input('Digite um número [999 para parar]: '))
print('Voce digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
