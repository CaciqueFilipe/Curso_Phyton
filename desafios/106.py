# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM' o programa se encerrará
#OBS. use cores.
def titulo(decorator, txt):
    tam = len(txt) + 4
    print(decorator * tam)
    print(f'  {txt}')
    print(decorator * tam)

while True:
    titulo('~', 'SISTEMA DE AJUDA PyHELP')
    resp = str(input('Função ou Biblioteca > '))
    if resp.upper() == 'FIM':
        titulo('~', 'ATÉ LOGO!')
        break
    
    titulo('~', f"Acessando o manual do comando '{resp}'")
    help(resp)


