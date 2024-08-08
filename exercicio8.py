'''8 - Faça um programa que peça o email e a senha para o usuário, o programa irá verificar se o usuário é igual a admin e a senha igual a 123, se sim mostrar
usuário logado, se não informar se o usuário ou senha ou ambos estão
incorretos.'''
email = "admin"
senha = "123"

emailVerificação = input("Digite o email: ")
senhaVerificação = input("Digite a senha: ")

if emailVerificação == email and senhaVerificação == senha: 
    print("Usuário logado")
elif emailVerificação != email and senhaVerificação == senha: 
    print("Usuário ou senha incorretos")
    print("Tente novamente ")
