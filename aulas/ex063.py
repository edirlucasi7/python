flag = False
contador = 0
total = 0
while not flag:
    numero = int(input('Digite um número: '))
    contador += 1
    total += numero
    if numero == 999:
        flag = True
        total = total - 999
        contador -= 1
print(contador)
print(total)
