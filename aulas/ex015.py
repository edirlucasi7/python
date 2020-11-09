import math
ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Seno > {:.2f}\n'.format(sen))
print('Cosseno > {:.2f}\n '.format(cos))
print('Tangente > {:.2f}\n '.format(tang))
