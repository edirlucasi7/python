nome = input('Qaul o seu nome:')
print('Seu nomo é {:*^20}!'.format(nome))

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
s = n1 + n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
m = n1 * n2
print('A soma é: {}, \nA divisão é: {:.3f}, A potência é: {}'.format(s, d, e), end=' >>>')
print('A divisão inteira é: {}, A multiplicação é: {}'.format(di, m))
