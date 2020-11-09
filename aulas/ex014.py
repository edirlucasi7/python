from math import pow
compCo = float(input('Digite o comprimento do cateto oposto: '))
compCa = float(input('Digite o comprimento do cateto adjacente: '))
compH = (pow(compCo, 2) + pow(compCa, 2)) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(compH))
