numero = int(input('Digite a quantidade de elementos: '))
i = 0
j = 1
total = 0
saida = 2
while saida < numero:
    if i == 0:
        print('0 => 1', end='')
    total = i + j
    i = j
    j = total
    print(' => {}'.format(total), end='')
    saida += 1
