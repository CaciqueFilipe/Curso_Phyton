# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento)
# e mostre a área do terreno

def área(largura, comprimento):
    return (largura * comprimento)


print('CONTROLE DE TERRENOS')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area = área(largura, comprimento)
print(f'A área de um terreno {largura}x{comprimento} é de {area:5.1f}m²')

'''
# Gustavo - Outra forma
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
'''