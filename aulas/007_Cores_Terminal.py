import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores


## Exemplos

# Escrever a palavra "Teste" com fundo vermelho e letra branca:
# `\033[0;30;41m`
print("\033[0;30;41mTeste!\033[m")

# Escrever a palavra "Teste" sublinhado com fundo azul e letra amarela:
# `\033[4;33;44m`
print("\033[4;33;44mTeste!\033[m")

# Escrever a palavra "Teste" negrito com fundo amarelo e letra roxa:
# `\033[1;35;43m`
print("\033[1;35;43mTeste!\033[m")

# Escrever a palavra "Teste" com fundo preto e letra branca:
# `\033[m`
print("\033[mTeste!\033[m")

# Escrever a palavra "Teste" negrito com fundo branco e letra preta:
# `\033[7;30m`
print("\033[7;30mTeste!\033[m")

a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a, b))

nome = "Cores 1 "
print(
    "Olá! Muito prazer em te conhecer, {}{}{}!!!".format("\033[4;31m", nome, "\033[m")
)


print(
    "Olá! Muito prazer em te conhecer, {}{}{}!!!".format(
        cores["amarelo"]["amarelo"], nome, cores["limpa"]
    )
)

nome = "Cores 2 "
print(
    "Olá! Muito prazer em te conhecer, {}{}{}!!!".format(
        cores["branco"]["fundoBrancoTextoVerdeSublinhado"], nome, cores["limpa"]
    )
)
