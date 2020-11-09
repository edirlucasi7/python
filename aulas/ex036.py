numero = int(input('Digite um número: '))
opcao = int(input('Digite sua opção de conversão: '))
print('Opção escolhida: {:*^20}'.format(opcao))
if opcao == 1:
    print('\033[1;30mDecimal: {}\033[m'.format(bin(numero)))
elif opcao == 2:
    print('\033[1;31mOctal: {}\033[m'.format(oct(numero)))
elif opcao == 3:
    print('\033[1;34mHexadecimal: {}\033[m'.format(hex(numero)))

