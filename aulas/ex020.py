nomeCompleto = (input('Digite seu nome: ')).strip()
print('{}'.format(nomeCompleto.upper()))
print('{}'.format(nomeCompleto.lower()))
print('{}'.format(len(nomeCompleto) - nomeCompleto.count(' ')))
qtd = nomeCompleto.split()
# print('{}'.format(nomeCompleto.find(' ')))
print(len(qtd[0]))

