precoOriginal = float(input('Digite o preco original do produto: '))
desconto = int(input('Digite o desconto que o produto irá receber: '))
valorDescontado = precoOriginal * (desconto / 100)
precoDesconto = precoOriginal - valorDescontado

print(f'Preço original: R${precoOriginal:.2f}', sep='')
print(f'Valor descontado: R${valorDescontado:.2f}', sep='')
print(f'Preço com desconto: R${precoDesconto:.2f}', sep='')