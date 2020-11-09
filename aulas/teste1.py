vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Digite o valor a ser procurado: "))
i = 1
while i <= len(vetor):
    if x == i:
        i = len(vetor) + 2
    else:
        i += 1
if i == len(vetor) + 2:
    print("Encontrei", x)
if i == len(vetor) + 1:
    print("Número não encontrado")
