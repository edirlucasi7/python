# nota1 = float(input('Digite sua nota na primeira prova: '))
# nota2 = float(input('Digite sua nota na segunda prova: '))
# media = (nota1 + nota2) / 2
# if media <= 7:
#     print('Aluno Reprovado: {:.2f}'.format(media))
# else:
#     print('O aluno passou de ano! {:.2f}'.format(media))

nome = str(input('Digite seu nome: ')).strip()
nomeSplit = nome.split()
nomeSplit[0]
# print(len(nomeSplit))
nomeSplit[len(nomeSplit) - 1]
print("""Caso o usuário não informa nome de perfil preferido o nome será: {}""".format(nomeSplit[0] + ' ' +
                                                                                       nomeSplit[len(nomeSplit) - 2]))



