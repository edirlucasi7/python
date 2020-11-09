n = 'S'
while n == 'S':
    input('Digite um valor: ')
    n = input('Vc deseja continuar [S/N]: ').upper()

# n = 1
# while n < 4:
#     input('Digite seu nome: ')

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print('A quantidade de números pares é: {}'.format(par))
print('A quantidade de números ímpares é: {}'.format(impar))
