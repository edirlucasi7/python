num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
if num1 < num2:
    maior = num2
    print(maior)
elif num2 < num1:
    maior = num1
    print(maior)
else:
    print('Valores iguais')


