import random
lista = [1, 2, 3, 4, 5]
numeroComputador = random.choice(lista)
# print(numeroComputador)
numeroUsuario = int(input('Digite um número: '))
if numeroComputador == numeroUsuario:
    print('Você VENCEU!!!!! O número escolhido pela máquina foi: {} e o escolhido por você foi: {} '.format
          (numeroComputador, numeroUsuario))
else:
    print('Você ERROUU o número!!! O número escolhido pela máquina foi: {} e o escolhido por você foi: {} '.format
          (numeroComputador, numeroUsuario))

