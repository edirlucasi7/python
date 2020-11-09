nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('\033[1;31mREPROVADO')
elif 5 < media < 6.9:
    print('\033[1;30mRECUPERAÇÃO')
else:
    print('\033[1;32mAPROVADO')
