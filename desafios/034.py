# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores à R$1250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salário do funcionario:'))

if salario <= 1250:
    print("Se novo salario com aumento de 15% será {:.2f}".format(
        salario + (salario * 15 / 100)
    ))
else:
    print("Se novo salario com aumento de 10% será {:.2f}".format(
        salario + (salario * 10 / 100)
    ))

'''
## Outra opção sugerida pelo Gustavo:

print("\n{:=^20}".format(" Gustavo "))
salario = float(input('Digite o salário do funcionario:'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, novo)))
'''
