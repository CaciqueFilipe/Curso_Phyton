# Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
# Para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    print('=' * 20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 20)
    if n < 0:
        break
    c = 1
    while c <= 10:
        print("{} x {} = {}".format(n, c, n * c))
        c += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
