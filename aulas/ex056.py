mediaIdade = 0
homemMaisVelho = 0
contadorMulher = 0
for f in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Difgite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).upper()
    mediaIdade += idade/4
    if 'M' in sexo or 'MASCULINO' in sexo:
        if f == 1:
            homemMaisVelho = idade
        else:
            if idade > homemMaisVelho:
                homemMaisVelho = idade
    if 'F' in sexo or 'FEMININO' in sexo:
        if idade < 20:
            contadorMulher += 1
print(mediaIdade)
print(homemMaisVelho)
print(contadorMulher)
