numero_primo = int(input('Digite o número: '))
contador = 0
for c in range(1, numero_primo + 1):
    if numero_primo % c == 0:
        contador += 1
if contador == 2:
    print('O número é primo: {}'.format(numero_primo))
