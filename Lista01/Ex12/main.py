from math import pi

raioDentro = int(input('Digite o valor do raio interno: '))
raioFora = int(input('Digite o valor do raio externo: '))

while raioDentro >= raioFora:
    print('Raio interno deve ser menor que o raio externo!\n')

    raioDentro = int(input('Digite o valor do raio interno: '))
    raioFora = int(input('Digite o valor do raio externo: '))


areaCirculoDentro = pi * (raioDentro ** 2)
areaCirculoFora = pi * (raioFora ** 2)

coroa = areaCirculoFora - areaCirculoDentro

print(f'Área da coroa: {coroa:.2f}')
