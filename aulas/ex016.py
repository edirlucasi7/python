import random
# aluno1 = input('Digite o nome da primeiro pessoa: ')
# aluno2 = input('Digite o nome da segundo pessoa: ')
# aluno3 = input('Digite o nome da terceiro pessoa: ')
# aluno4 = input('Digite o nome da quarto pessoa: ')
alunoAleatorio = ['Yuri', 'Luara', 'Lucas', 'Marcos', 'Mara', 'Talita', 'Karine', 'Janderson',
                  'Yasmin', 'Meire', 'Maria', 'Yarice']
sorteio = random.choice(alunoAleatorio)
sorteio1 = random.choice(alunoAleatorio)
sorteio2 = random.choice(alunoAleatorio)
print('O pessoa sorteado foi: {:*^20} {:*^20} {:*^20}'.format(sorteio, sorteio1, sorteio2))
