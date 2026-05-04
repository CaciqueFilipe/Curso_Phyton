# Escreva um programa que leia um valor em metros e o exiva convertido em centimetros e milimetros

n = float(input("Digite um valor em metros:"))
cm = n * 100
mm = n * 1000
print("{}m corresponde a {}cm e {}mm.".format(n, cm, mm))   