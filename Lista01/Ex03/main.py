qtdeCopias = int(input('Digite a quantidade de copias: '))

while qtdeCopias <= 0:  # impede o usuário de digitar um valor menor que 0
    qtdeCopias = int(input('Digite um valor válido: '))

precoBiblio = 24.95 * 0.65  # preco para bibliotecas (desconto de 35%)
precoTotal = 3 + ((qtdeCopias - 1) * 0.75) + precoBiblio

print(f'Custo total da compra: R${precoTotal:.2f}')