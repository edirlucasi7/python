numero = int(input('Digite um número para calcular seu fatorial: '))
# if numero == 0:
#     print('1')
# else:
#     for f in range(numero - 1, 1, -1):
#         numero *= f
# if numero != 0:
#     print(numero)
f = numero
if numero == 0:
    print('1')
else:
    while f != 1:
        numero *= f - 1
        f -= 1
if numero != 0:
    print(numero)
