qtdKm = float(input('Quantos Km o seu carro percorreu? '))
qtdD = float(input('Por quantos dias seu carro foi alugado? '))
precoKm = qtdKm * 0.15
precoD = qtdD * 60
print('Você rodou {:.0f}Km por {:.0f} dias e precisa pagar o valor de R${:.2f}'.format(qtdKm,
      qtdD, precoKm + precoD))

