from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8):
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        cont += 1
    else:
        cont1 += 1
print('Não atigiram a maior idade: {}'.format(cont1))
print('Atigiram a maior idade: {}'.format(cont))

