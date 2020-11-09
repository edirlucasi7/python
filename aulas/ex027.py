vel = float(input('Digite a velocidade do carro: '))
velUltra = vel - 80
if vel > 80:
    print('MULTADO!! Velocidade: {:.2f}Km -->> Multa: R${}'.format(vel, velUltra * 7))

