# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome completo:")
print("Seu nome com todas letras maisculas: {}".format(nome.upper()))
print("Seu nome com todas letras minusculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
nome = str(input("Digite o seu nome completo:")).strip()
print('Analisando seu nome...')
print("Seu nome em maisculas: {}".format(nome.upper()))
print("Seu nome em minusculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
#Outra opção
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))
'''
