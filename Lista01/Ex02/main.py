valorFinal = float(input('Digite o valor final desejado: '))
qtdeMeses = int(input('Digite o numero de meses: '))
rentMensal = float(input('Digite a rentabilidade mensal: '))

valorInicial = valorFinal / ((1 + (rentMensal / 100)) ** qtdeMeses)

print(f'Valor inicial necessário: R${valorInicial:.2f}')
