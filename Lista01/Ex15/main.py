alturaTriangulo = int(input('Digite o raio do hexágono: '))
baseTriangulo = int(input('Digite a medida do lado do hexágono: '))

areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
areaHexagono = areaTriangulo * 6

print(f'Área do hexágono: {areaHexagono:.2f}')