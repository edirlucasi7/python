from datetime import date

data_nascimento = int(input('Digite seu ano de nascimento: '))
conferir_aniversario = int(input('Digite 1 se já fez aniversário esse ano e 2 se não fez: '))
ano_atual = date.today().year

if conferir_aniversario == 1:
    idade = ano_atual - data_nascimento
else:
    idade = ano_atual - data_nascimento + 1

if idade < 10:
    print('\033[1;32mMIRIM')
elif idade < 15:
    print('\033[1;33mINFANTIL')
elif idade < 20:
    print('\033[1;34mJÚNIOR')
elif idade < 21:
    print('\033[1;35mSÊNIOR')
else:
    print('\033[1;36mMASTER')
