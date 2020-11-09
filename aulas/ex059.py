num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] subtrair\n[ 4 ] dividir\n[ 5 ] sair do programa')
    opcao = int(input('\033[1;34mDigite uma oção: \033[m'))
    if opcao == 1:
        resultado = num1 + num2
        print('A soma é {}'.format(resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('A multiplicação é {}'.format(resultado))
    elif opcao == 3:
        resultado = num1 - num2
        print('A subtração é {}'.format(resultado))
    else:
        resultado = num1 / num2
        print('A multiplicação é {}'.format(resultado))
