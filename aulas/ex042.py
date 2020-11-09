altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2
print(imc)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc < 25:
    print('Peso Ideal')
elif 24 < imc < 31:
    print('Sobrepeso')
elif 30 < imc < 41:
    print('Obesidade')
else:
    print('Obesidade mórbida')
