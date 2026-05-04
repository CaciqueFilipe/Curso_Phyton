# Faça um algoritmo que leia o salario do funcionário e mostre seu novo salario com 15% de aumento.

salario = float(input("Qual o salário do funcionário?"))
aumento = salario + (salario * 15 / 100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.".format(salario, aumento))    