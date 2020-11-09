nomeCadastro = str(input(("Cadastre o nome do seu usuário: "))).upper().split()

print("--------------------LOGIN-----------------")

nome = str(input(("Digite o nome do seu usuário: "))).upper().split()

if (nomeCadastro == nome):
    print("\033[0:36mUsuário logado com sucesso\033[m")
else:
    print("\033[0:31mUsuário inválido\033[m")
