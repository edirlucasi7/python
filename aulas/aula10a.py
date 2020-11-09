print('\033[0;31;43mOlá Mundo!\033[m')
nome = 'Lucacs Icety'
cores = {
    'limpa':'\033[m',
    'azul':'\033[1;34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m'
}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))
