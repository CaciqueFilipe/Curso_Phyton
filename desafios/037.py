# Escreva um programa que leia um número inteiro e peça par o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# Apenas para usar a pasta cores
import sys
import os
from time import sleep
# Adiciona a pasta raiz do projeto ao sys.path para que o Python encontre o pacote 'cores'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cores.cores import cores

print('{}CONVERSOR DE NÚMERO{}'.format(
    cores["amarelo"]["fundoAmareloTextoVermelhoNegrito"],
    cores["limpa"]
))

# Lendo o número inteiro
num = int(input('Digite um número inteiro: '))

# Exibindo o menu de opções
print('''{}Escolha uma das bases para conversão:{}
{}[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL{}'''.format(
    cores['amarelo']['amareloNegrito'],
    cores['limpa'],
    cores['vermelho']['fundoVermelhoTextoBrancoNegrito'],
    cores['limpa']
))

opcao = int(input('Sua opção: '))

# Lógica de conversão e exibição do resultado
if opcao == 1:
    # print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    # print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    # print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:].upper()}')
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente com 1, 2 ou 3.')
