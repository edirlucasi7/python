import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 0
numeroComputador = random.choice(lista)
print(numeroComputador)
numeroJogador = int(input('Digite um valor: '))

while numeroJogador != numeroComputador:
    numeroJogador = int(input('Digite um valor: '))
    contador += 1
print('{}'.format(contador + 1))
