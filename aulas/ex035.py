nome = str(input('Digite seu nome: '))
cpf = int(input('Informe seu cpf: '))
valorCasa = float(input('Digite o valor da casa: '))
salarioComprador = float(input('Digite o valor do seu salário: '))
anosPagamento = float(input('Em quantos anos será o pagamento: '))
valorParcela = valorCasa/(anosPagamento*12)
if valorParcela <= salarioComprador*0.3:
    print('\033[1;32;40mPARABÉNS, {}. CPF:{}!\033[m \033[4;34mSeu crédito foi aprovado.\033[m'.format(nome, cpf))
else:
    print('\033[1;31;40mDESCULPE! Seu crédito foi negado.\033[m')
