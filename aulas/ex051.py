primeiro_termo = int(input('Digite o primeiro termo da sua progressão aritimética: '))
razao = int(input('Digite a razão da sua progressão aritimética: '))
print(10*razao)
qtd_termos = primeiro_termo+(10*razao)
for c in range(primeiro_termo, qtd_termos, razao):
    print(c)

