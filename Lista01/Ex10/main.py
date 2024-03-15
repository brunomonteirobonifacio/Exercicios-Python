precoOriginal = float(input('Digite o preco original do produto: '))
valorDescontado = precoOriginal * .2
precoDesconto = precoOriginal - valorDescontado

print(f'Preço original do produto: R${precoOriginal:.2f}', sep='')
print(f'Valor descontado: R${valorDescontado:.2f}', sep='')
print(f'Preço com desconto: R${precoDesconto:.2f}', sep='')
