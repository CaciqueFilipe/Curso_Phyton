# Faça um programa que tenha uma função chamada escreva(),
# Que receba um texto qualquer como parâmetro
# E mostre uma mensagem com tamanho adaptável
#
# Ex:
#escreva('Olá,Mundo!')
#
# Saída
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~
def escreva(txt):
    tam = len(txt) + 4
    print('~'*tam)
    print(f'{txt:^}')
    print('~'*tam)


escreva('Olá,Mundo!')
escreva('Curso de Python no YouTube')
escreva('CeV')