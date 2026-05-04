# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2
print("A média entre {} e {} é igual a {:.1f}.".format(n1, n2, media))

## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
n1 = float(input("Primeira nota do aluno:"))
n2 = float(input("Segunda nota do aluno:"))
# phyton aceita variavel com acento
média = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}.".format(n1, n2, média))
