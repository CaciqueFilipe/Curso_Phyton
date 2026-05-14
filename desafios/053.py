# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo.
# Desconsiderando acentos e os espaços

# Ex: Posso ler normal e tras para frente:
# apos a sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anotaram a data da
# Maratona
# arara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # aqui junta sem espaços
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

