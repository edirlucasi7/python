primeiro_termo = int(input('Digite o primeiro termo da sua progressão aritimética: '))
razao = int(input('Digite a razão da sua progressão aritimética: '))
termo = primeiro_termo
cont = 1
mais_termos = 10
total = 0
while mais_termos != 0:
    total += mais_termos
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos a mais vc precisa? '))
print('Quantidade de termos: {}'.format(cont))
print('FIM')

