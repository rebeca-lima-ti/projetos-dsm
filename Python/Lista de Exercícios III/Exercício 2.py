#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    name = input("Entre com um nome de usuário: ")
    senha = input("Entre com uma senha para o usuário: ")

    if name == senha:
        print("Erro! Nome de usuário e senha devem ser diferentes!")
    else:
        print("Usuário e senha aceitos!")
        break