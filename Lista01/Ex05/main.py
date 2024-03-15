distancia = int(input('Digite a variação do deslocamento do objeto (metros): '))
tempo = int(input('Digite a variação de tempo percorrido (segundos): '))

velocidade = distancia / tempo

print(f'Velocidade média: {velocidade:.2f}m/s', sep='')
