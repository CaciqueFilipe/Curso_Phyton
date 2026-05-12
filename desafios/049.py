# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher.
# Só que agora utilizando o laço for

n = int(input("Digite um número para ver sua tabuada:"))

print("-" * 12)

for c in range(1, 10 + 1):
    print("{} x {} = {}".format(n, c, n * c))

print("-" * 12)