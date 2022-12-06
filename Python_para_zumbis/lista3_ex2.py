usuário = input("Usuário: ")
senha = input("Senha: ")
while usuário == senha:
    print("Senha deve ser diferente de usuário!")
    usuário = input("Usuário: ")
    senha = input("Senha: ")