mais = int(input('\033[1;31mQauntos números você quer digitar: \033[m'))
cont = 0
total = 0
media = 0
maior = 0
menor = 0
while mais != 0:
    total += mais
    while cont < total:
        numero = int(input('\033[1;36mDigite um número: \033[m'))
        cont += 1
        media += numero
        print(' -> {}'.format(numero))
        if cont == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    print('PAUSA')
    mais = int(input('Você precisa de mais quantos números? '))
print('{:.2f}'.format(media/cont))
print(menor)
print(maior)

