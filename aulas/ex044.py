import random
from time import sleep
print('-'*10+'POSSÍVEIS JOGADAS'+'-'*10)
print('PEDRA')
print('PAPEL')
print('TESOURA')
jogada_usuario = str(input('Qual sua jogada? ')).upper()
print('JOK')
sleep(1)
print('EN')
sleep(1)
print('PO')
jogada_aleatoria = ['PEDRA', 'PAPEL', 'TESOURA']
sorteio = random.choice(jogada_aleatoria)
print('Jogada Computador: {}'.format(sorteio))

if jogada_usuario == 'PEDRA':
    if sorteio == 'PAPEL':
        print('VENCEDOR: {}'.format(sorteio))
    elif sorteio == 'TESOURA':
        print('VENCEDOR: {}'.format(jogada_usuario))
    else:
        print('EMPATE')
elif jogada_usuario == 'PAPEL':
    if sorteio == 'PEDRA':
        print('VENCEDOR: {}'.format(jogada_usuario))
    elif sorteio == 'TESOURA':
        print('VENCEDOR: {}'.format(sorteio))
    else:
        print('EMPATE')
elif jogada_usuario == 'TESOURA':
    if sorteio == 'PEDRA':
        print('VENCEDOR: {}'.format(sorteio))
    elif sorteio == 'PAPEL':
        print('VENCEDOR: {}'.format(jogada_usuario))
    else:
        print('EMPATE')
