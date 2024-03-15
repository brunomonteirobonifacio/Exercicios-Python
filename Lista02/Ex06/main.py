from math import pi

raio = int(input('Digite o raio do circulo: '))

perimetro = 2 * pi * raio
area = pi * (raio ** 2)

print(f'Área do círculo: {area:.2f}')
print(f'Perímetro do círculo: {perimetro:.2f}')