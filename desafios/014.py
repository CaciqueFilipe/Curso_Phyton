# Crie um algoritmo que receba a temperatura em Cº e retorne em Fº

c = float(input('Informe a temperatura em Celsius:'))
f = 9 * c / 5 + 32 # Por causa da ordem de precedencia nao precisa de parenteses
print('A temperatura de {}ºC corresponde a {}ºF.'.format(c, f))