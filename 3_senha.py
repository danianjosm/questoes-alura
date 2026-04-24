# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos
#  correspondem aos valores esperados determinados por você.

nome = input("Digite o seu nome: ")
senha = int(input("Digite sua senha: "))

senha_correta = 1234
nome_correto = "carol" # as aspas são pra string

if nome == nome_correto and senha == senha_correta:
    print("login efetuado com sucesso")
else:
    print("Senha ou nome estão incorretos")