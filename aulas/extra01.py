tamanho = int(input('\033[1;35mDigite o tamanho da lista: \033[m'))
i = 0
menor = 0
maior = 0
while i < tamanho:
    valor = int(input('Digite um valor: '))
    if i == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    i += 1
print(menor)
print(maior)
