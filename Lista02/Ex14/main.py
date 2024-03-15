peso = float(input('Digite seu peso (em quilogramas): '))
altura = float(input('Digite sua altura (em metros): '))

imc = peso / (altura ** 2)

print(f'Seu IMC é de: {imc:.2f}')
print('Classificação: ', end='')

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print('Peso normal')
elif 25 <= imc <= 29.9:
    print('Acima do peso')
elif 30 <= imc <= 34.9:
    print('Obesidade grau I')
elif 35 <= imc <= 40:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')