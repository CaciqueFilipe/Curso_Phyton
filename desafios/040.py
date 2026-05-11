# Crie um programa que leia duas notas de um aluno e calcule sua média
# Mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

print(
    "{}CALCULO DE MÉDIA{}".format(
        cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"], cores["limpa"]
    )
)

n1 = float(
    input(
        "{}Primeira nota do aluno: {}".format(
            cores["branco"]["brancoNegrito"], cores["limpa"]
        )
    )
)
n2 = float(
    input(
        "{}Segunda nota do aluno: {}".format(
            cores["branco"]["brancoNegrito"], cores["limpa"]
        )
    )
)

média = (n1 + n2) / 2
print(
    "{}A média entre {:.1f} e {:.1f} é igual a {:.1f}.{}".format(
        cores["azul"]["azulNegrito"], n1, n2, média, cores["limpa"]
    )
)

if 7 > média >= 5:
    print("{}RECUPERAÇÃO{}".format(cores["amarelo"]["amareloNegrito"], cores["limpa"]))
elif média < 5:
    print("{}REPROVADO{}".format(cores["vermelho"]["vermelhoNegrito"], cores["limpa"]))
else:
    print("{}APROVADO{}".format(cores["verde"]["verdeNegrito"], cores["limpa"]))
