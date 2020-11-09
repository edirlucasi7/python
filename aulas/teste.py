vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
menor = vetor[0]
maior = vetor[8]
y = False
x = int(input("Digite o valor a ser procurado: "))
if x > 10:
    print("número não encontrado")
    y = True
while not y:
    i = int(menor + (maior - menor)/2)
    if x == vetor[i]:
        print("Valor encontrado", x)
        y = True
    if x < vetor[i]:
        maior = i-1
    else:
        menor = i + 1




