print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
pReta = float(input('Qual o comprimento da primeira reta: '))
sReta = float(input('Qual o comprimento da segunda reta: '))
tReta = float(input('Qual o comprimento da terceira reta: '))
valor1 = abs(sReta - tReta)
valor2 = abs(pReta - tReta)
valor3 = abs(pReta - sReta)

if valor1 < pReta < sReta+tReta and valor2 < sReta < pReta+tReta and valor3 < tReta < pReta + sReta:
    print('Os comprimentos das retas podem formar um triângulo: {}, {}, {}'.format(pReta, sReta, tReta))
    if pReta == sReta == tReta:
        print('Equilátero')
    elif pReta != sReta != tReta:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não é possível formar uma reta com os comprimentos informados!')


