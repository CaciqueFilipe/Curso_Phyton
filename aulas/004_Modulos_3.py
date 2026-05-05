# Importando apenas especifico do módulo
# from math import sqrt
# Importar mais de um
from math import sqrt, floor

num = int(input("Digite um numero: "))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
