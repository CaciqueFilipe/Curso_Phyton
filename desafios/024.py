# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Digite o nome de uma cidade:").strip()
comeca = cidade[:5].upper() == "SANTO"
print("Sua cidade começa com SANTO? {}".format(comeca))
