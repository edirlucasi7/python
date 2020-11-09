from random import randint
numeroComputador = randint(1, 10)
contador = 0
acertou = False
while not acertou:
    jogador = int(input('Digite um valor: '))
    contador += 1
    if jogador == numeroComputador:
        acertou = True
print('O número que o computador escolheu foi {} e o número que o jogador escolheu foi {}.'
      ' Foram necessárias {} tentativas.'.format(numeroComputador, jogador, contador))
