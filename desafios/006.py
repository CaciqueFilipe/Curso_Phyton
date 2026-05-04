# Faça um programa que leia um numero e mostre seu dobro, seu triplo e raiz quadrada

n = int(input("Digite um número:"))
dobro = n * 2
triplo = n * 3
raizQuadrada = n ** (1 / 2)

print(
    "Analisando o valor {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.".format(
        n, dobro, triplo, raizQuadrada
    )
)

## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
print("O dobro de {} vale {}".format(n, dobro))
print(
    "O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}".format(
        n, triplo, n, raizQuadrada
    )
)

# Outra forma com calculos no format

print("\n{:=^20}".format(" Outra forma "))
print("O dobro de {} vale {}".format(n, (n * 2)))
print(
    "O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}".format(
        n,
        (n * 3),
        n,
        (n**(1 / 2)) # Ou com pow(n, (1/2))
    )
)