preco_produto = float(input('Digite o valor do produto: '))
print('-'*10+'FORMA DE PAGAMENTO'+'-'*10)
print('1: DINHEIRO')
print('2: CHEQUE')
print('3: À VISTA NO CARTÃO -> 5% DE DESCONTO')
print('4: 2x NO CARTÃO')
print('5: 3x OU MAIS -> 205 DE JUROS')
condicao_pagamento = int(input('Digite a condição de pagamento: '))
if condicao_pagamento == 1 or condicao_pagamento == 2:
    valor_final = preco_produto*0.9
elif condicao_pagamento == 3:
    valor_final = preco_produto*0.95
elif condicao_pagamento == 4:
    valor_final = preco_produto
else:
    valor_final = preco_produto*1.20
print('O valor do seu produto com a condição de pagamento Nº: {} é {:.2f}'.format(condicao_pagamento, valor_final))
