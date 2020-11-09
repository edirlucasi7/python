salario = float(input('Digite o seu salário: '))
if salario > 1250:
    resultado = salario * 1.10
else:
    resultado = salario * 1.15
print('O rersultado é: {:.2f}'.format(resultado))
