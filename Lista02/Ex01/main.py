def calcularValorFuturo():
    valorInicial = float(input('Digite o valor inicial: '))
    qtdeMeses = int(input('Digite o numero de meses: '))
    rentMensal = float(input('Digite a rentabilidade mensal: '))

    valorFinal = valorInicial * (1 + (rentMensal / 100)) ** qtdeMeses

    return valorFinal


def calcularValorInicial():
    valorFinal = float(input('Digite o valor final desejado: '))
    qtdeMeses = int(input('Digite o numero de meses: '))
    rentMensal = float(input('Digite a rentabilidade mensal: '))

    valorInicial = valorFinal / ((1 + (rentMensal / 100)) ** qtdeMeses)

    return valorInicial


# ========================================= #

print('[ 1 ] Calcular valor futuro')
print('[ 2 ] Calcular valor inicial')

match input('Digite a opção desejada: '):
    case '1':
        print('\nCalcular valor futuro')
        print('\n*********************\n')

        print(f'Valor futuro: R${calcularValorFuturo():.2f}')

    case '2':
        print('\nCalcular valor inicial')
        print('\n*********************\n')

        print(f'Valor inicial: R${calcularValorInicial():.2f}')

    case _:  # '_' == 'else'
        print('Opção inválida')
