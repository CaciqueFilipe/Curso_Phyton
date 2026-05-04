# Escreva um programa que leia um valor em metros e o exiva convertido em centimetros e milimetros

n = float(input("Digite um valor em metros:"))
cm = n * 100
mm = n * 1000
print("{}m corresponde a {:.0f}cm e {:.0f}mm.".format(n, cm, mm))

## Outra opção sugerida pelo Gustavo:

## Escala
### km hm dam m dm cm mm

print("\n{:=^20}".format(" Gustavo "))
medida = float(input("Uma distância em metros:"))
cm = medida * 100
mm = medida * 1000
print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm.".format(medida, cm, mm))
