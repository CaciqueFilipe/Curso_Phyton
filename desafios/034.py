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
