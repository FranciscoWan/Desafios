import time
import json
import os

tentativas = 3

nome_arquivo = "credenciais.json"
data = 0

if os.path.exists(nome_arquivo):
    with open ("credenciais.json", "r") as file:
        data = json.load(file)
        nome_set = data["nome_set"]
        senha_set = data["senha_set"]
        dica = data["dica"]
else:
    nome_set = input("Crie o nome de login do sistema: ")
    senha_set = input("Escolha uma senha para acessar o sistema: ")
    dica = input("Digite uma dica para caso esqueça sua senha: ")
    credenciais = {"nome_set": nome_set,
                   "senha_set": senha_set,
                   "dica": dica}
    with open ("credenciais.json", "w") as file:
        json.dump(credenciais, file, indent=4)
    
if data:
    print("Escolha uma opção: ")
    op = input('''1 - Entrar
2 - Sair 
opção: ''')
    if op == "1":
        print("Acessando sistema", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        while tentativas > 0:
            print("\n")
            print("#"*20)
            print("Digite as credenciais - ")
            nome = input("Login: ")
            senha = input("Password: ")
            print("#"*20)
            if nome == nome_set and senha == senha_set:
                print("Bem vindo ao sistema!")
                break
            elif nome != nome_set and senha != senha_set:
                print("Acesso ao sistema negado!")
                tentativas -= 1
                if tentativas == 2:
                    print(f"Sua senha está incorreta. A dica é: {dica}")
                elif tentativas == 0:
                    print("Você excedeu o número de tentativas. Programa encerrado.")
                    break
            else:
                print("Seu impostor! Programa encerrado")
                break
            print(f"Você ainda possui {tentativas} tentativas para acertar a senha.")
    elif op == "2":
        print("Programa encerrado.")
    else: 
        print("opção inválida, escolha novamente.")

