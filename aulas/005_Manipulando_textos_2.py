
frase = 'Curso em Video Python'
print(frase)

## Fatiamento

frase1 = frase[9]
print(frase1) # Saida V

frase2 = frase[9:13]
print(frase2) # Saida Vide

frase3 = frase[9:21]
print(frase3) # Saida 

frase4 = frase[9:21:2]
print(frase4) # Saida V

frase5 = frase[:5]
print(frase5) # Saida V

frase6 = frase[15:]
print(frase6) # Saida V

frase7 = frase[9::3]
print(frase7) # Saida V

## Função len
print(len(frase))

## Função count
print(frase.count('o'))
print(frase.count('o', 0, 13))

## Função find
print(frase.find('deo'))
print(frase.find('android'))

## Operador in
print('Curso' in frase)
print('Android' in frase)

## Transformação

### Replace
frase8 = frase.replace('Python', 'Android')
print(frase8)

### Upper)
frase9 = frase.upper()
print(frase9)

### Lower
frase10 = frase.lower()
print(frase10)

### Capitalize
frase11 = frase.capitalize()
print(frase11)

### Title
frase12 = frase.title()
print(frase12)

## Strip
fraseTeste1 = '   Aprendendo Python  '
fraseTeste1.strip()
print(fraseTeste1)
# Saida 'Aprendendo Python'

### RStrip
fraseTeste2 = '   Aprendendo Python  '
fraseTeste2.rstrip()
print(fraseTeste2)
# Saida '   Aprendendo Python'

### LStrip
fraseTeste3 = '   Aprendendo Python  '
fraseTeste3.lstrip()
print(fraseTeste3)
# Saida 'Aprendendo Python  '

## Divisão

### Split
fraseTeste4 = frase.split()
print(fraseTeste4)
# Saida ['Curso', 'em', 'Video', 'Python']

### Join
fraseTeste5 = '-'.join(frase)
print(fraseTeste5)
# Saida 'Curso-em-Video-Python'

