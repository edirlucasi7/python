from datetime import date

data_nascimento = int(input('Digite seu ano de nascimento: '))
conferir_aniversario = int(input('Digite 1 se já fez aniversário esse ano e 2 se não fez: '))
ano_atual = date.today().year

if conferir_aniversario == 1:
    idade = ano_atual - data_nascimento
    tempo_restante = 18 - idade
else:
    idade = ano_atual - data_nascimento + 1
    tempo_restante = 18 - idade

if idade < 18:
    print('\033[4;30mNão está em tempo de alistar-se. Faltam {} anos.'.format(abs(tempo_restante)))
elif idade == 18:
    print('\033[4;32mEstá em tempo de alistar-se. Procure a junta militar mais próxima.')
else:
    print('\033[4;31mVocê já passou do tempo de alistar-se. Passaram {} anos.'.format(abs(tempo_restante)))
