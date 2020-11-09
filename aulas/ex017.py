# import random
# aluno1 = str(input('Digite o nome da primeiro pessoa: '))
# aluno2 = str(input('Digite o nome da segundo pessoa: '))
# aluno3 = str(input('Digite o nome da terceiro pessoa: '))
# aluno4 = str(input('Digite o nome da quarto pessoa: '))
# aleatoria = [aluno1, aluno2, aluno3, aluno4]
# random.shuffle(aleatoria)
# print(aleatoria)

import random
aluno1 = input('Digite o nome da primeira pessoa: ')
aluno2 = input('Digite o nome da segunda pessoa: ')
aluno3 = input('Digite o nome da terceira pessoa: ')
aluno4 = input('Digite o nome da quarta pessoa: ')
lista = [aluno1, aluno2, aluno3, aluno4]
aleatorio = random.sample(lista, 4)
print(aleatorio)




