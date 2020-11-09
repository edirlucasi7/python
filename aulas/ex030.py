ano = float(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano é Bissexto: {:.0f}'.format(ano))
if ano % 4 != 0:
    if ano % 400 != 0:
        print('O ano não é Bissexto'.format(ano))
    else:
        print('É Bissexto: {}'.format(ano))