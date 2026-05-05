# Faça um programa que leia o nome completo de uma pessoa.
# Mostrando em seguida o primeiro e o último nome separadamente.
# Ex:
# Ana Maria de Souza
# primeiro: Ana
# último: Souza

nome = input("Digite o seu nome completo:").strip()
nomes = nome.split()
quantidade = len(nomes)
print('Primeiro nome: {}'.format(nomes[0]))
print('Ultimo nome: {}'.format(nomes[quantidade - 1]))