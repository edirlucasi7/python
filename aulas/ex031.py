num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
if num1 > num2 and num1 > num3:
    maior = num1
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3
if num1 < num2 and num1 < num3:
    menor = num1
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3
print('O menor é: {}\nO maior é: {}'.format(menor, maior))
