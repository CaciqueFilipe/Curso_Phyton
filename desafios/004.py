# Crie um script Python que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele.

key = input("Digite algo:")
print("O tipo primitivo desse valor é:", type(key))
print("Só tem espaços?", key.isspace())
print("É um número?", key.isnumeric())
print("É alfabético?", key.isalpha())
print("É alfanumérico?", key.isalnum())
print("Está em maiúsculas?", key.isupper())
print("Está em minúsculas?", key.islower())
print("Está capitalizada?", key.istitle())
