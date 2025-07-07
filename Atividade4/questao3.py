while True:
    senha = input("Digite uma senha forte ou 'sair' para encerrar: ")

    if senha.lower() == 'sair':
        print("Encerrando verificação.")
        break

    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte! ✅")
        break
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
