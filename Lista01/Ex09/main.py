preco = float(input('Digite o valor que será gasto com combustível (preco do combustivel: R$4.95): '))

litros = preco / 4.95
quilometros = 20 * litros

print(f'Litros de gasolina disponíveis por R${preco:.2f}: {litros:.2f}L', sep='')
print(f'O carro consegue rodar {quilometros:.2f}Km', sep='')
