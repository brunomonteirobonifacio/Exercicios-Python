valorInicial = float(input('Digite o valor inicial: '))
qtdeMeses = int(input('Digite o numero de meses: '))
rentMensal = float(input('Digite a rentabilidade mensal: '))

valorFinal = valorInicial * (1 + (rentMensal / 100)) ** qtdeMeses
print(f'Valor futuro: R${valorFinal:.2f}')