distancia = float(input('Quantos Km percorridas: '))
precoViagem1 = distancia * 0.5
precoViagem2 = distancia * 0.45
if distancia <= 200:
    print('Valor a ser pago: {:.2f}'.format(precoViagem1))
else:
    print('Valor a ser pago: {:.2f}'.format(precoViagem2))
