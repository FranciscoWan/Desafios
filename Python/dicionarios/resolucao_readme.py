# Resolução dos exercícios Readme.md

# Exercicio 1 
agenda_telefonica = {}
for i in range(3):
    nome = str(input("Digite o nome do contato: "))
    telefone = str(input(f"Digite o telefone do contato {nome}: "))
    agenda_telefonica[nome] = telefone
print(agenda_telefonica)


# Exercicio 2
frase = input("Digite uma frase: ")
palavras = frase.split(" ") # Separa as palavras da frase e cria uma lista com as palavras separando por espaço.
contador_palavras = {}
for palavra in palavras:
    contador_palavras[palavra] = palavras.count(palavra)
print(contador_palavras)


# Exercicio 3
dicionario_produtos = {}
n_produtos = int(input("Digite quantos produtos deseja adicionar: "))
for i in range(n_produtos):
    nome_produto = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o valor do produto {nome_produto}: "))
    dicionario_produtos[nome_produto] = preco
nome_procurado = input("Qual produto deseja verificar o preço: ")
for c, v in dicionario_produtos.items():
    if nome_procurado in dicionario_produtos:
        if c == nome_procurado:
            print(f"O produto {c} está custando {v}")
    else:
        print(f"O produto {nome_procurado} não foi cadastrado.")
        break


# Exercicio 4
notas_alunos = {}
qtd_alunos = int(input("Quantos alunos deseja inserir: "))
maior_nota = float("-inf")
menor_nota = float("inf")
for i in range(qtd_alunos):
    nome = input(f"Nome do {i+1}º aluno: ")
    nota = float(input(f"Nota do aluno {nome}: "))
    notas_alunos[nome] = nota
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

print("Cadastro de notas de alunos:")
print(f"{notas_alunos}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")


# Exercicio 5
dicionario_letras = {}
frase = input("Digite uma frase para contar as letras: ")
lista_palavras = frase.split(" ")
for palavra in lista_palavras:
    for letra in palavra:
        dicionario_letras[letra] = frase.count(letra)

print(dicionario_letras)


# Exercício 6
# Resolução 1 -
loja_virtual = {}
qtd_produtos = int(input("Digite a quantidade de produtos que irá inserir na loja: "))
soma_total = 0
for i in range(qtd_produtos):
    nome_produto = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço do produto {nome_produto}: "))
    soma_total += preco
    loja_virtual[nome_produto] = preco
print(f"A compra total ficou no valor de: R${soma_total}")

# Resolução 2 - 
loja_virtual = {}
qtd_produtos = int(input("Digite a quantidade de produtos que irá inserir na loja: "))
for i in range(qtd_produtos):
    nome_produto = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço do produto {nome_produto}: "))
    loja_virtual[nome_produto] = preco
soma_total = sum(loja_virtual.values())
print(f"A compra total ficou no valor de: R${soma_total}")


# Exercício 7
dicionario_usuario = {"nome": "Pedro", "idade": 20, "altura": 1.70}
dicionario_invertido =  {valor: chave for chave, valor in dicionario_usuario.items()}
print(dicionario_invertido)


# Exercício 8
boletim_alunos = {}
qtd_alunos = int(input("Digite a quantia de alunos que irá inserir: "))
for i in range(qtd_alunos):
    nome = input("Digite o nome do aluno: ")
    for j in range(3):
        lista_notas = []
        nota = float(input(f"Digite a {j+1} nota: "))
        lista_notas.append(nota)
    boletim_alunos[nome] = lista_notas

for c,v in boletim_alunos.items():
    media = sum(v)/len(v)
    if media >= 7:
        print(f"Aluno {c} APROVADO com média - {media}")
    elif media >= 5:
        print(f"Aluno {c} em RECUPERAÇÃO com média - {media}")
    else:
        print(f"Aluno {c} REPROVADO com média - {media}")


# Exercício 9
texto = input("Digite uma frase: ")
palavras  = texto.split(" ")
tam_palavra_longa = float('-inf')
tam_palavra_curta = float('inf')
qtd_python = 0
estatistica_texto = {}
estatistica_texto["total_palavras"] = len(palavras)
for i in palavras:
    if len(i) > tam_palavra_longa:
        estatistica_texto["palavra_mais_longa"] = i
        tam_palavra_longa = len(i)
        palavra_longa = i
    if len(i) < tam_palavra_curta:
        estatistica_texto["palavra_curta"] = i
        tam_palavra_curta = len(i)
        palavra_curta = i
    if i.lower() == "python":
        qtd_python += 1
        estatistica_texto["qtd_python"] = qtd_python

print(estatistica_texto)


# Exercício 10
sistema_cadastro = {}
print("-----Bem-vindo ao sistema de cadastro-----")
while True:
    print('''
1 - Cadastrar usuário
2 - Fazer login
3 - Alterar senha
4 - Excluir conta
5 - Listar usuários
6 - Sair
''')
    opc = int(input("Digite a opção: "))
    if opc == 1:
        nome = input("Nome de usuário: ")
        senha = input("Senha: ")
        sistema_cadastro[nome] = senha
    elif opc == 2:
        nome_login = input("Deseja realizar login com qual nome de usuário: ")
        if nome_login in sistema_cadastro:
            for c, v in sistema_cadastro.items():
                if c == nome_login:
                    senha_login = input("Digite a senha de login: ")
                    if senha_login == v:
                        print(f"Acesso permitido, bem vindo {c}")
                    else:
                        print("Acesso negado!")
        else:
            print("Login não encontrado")
    elif opc == 3:
        login_alterar_senha = input("Digite o login que deseja alterar a senha: ")
        if login_alterar_senha in sistema_cadastro:
            for c, v in sistema_cadastro.items():
                if c == login_alterar_senha:
                    nova_senha = input("Digite a nova senha: ")
                    sistema_cadastro[c] = nova_senha
                    print("Senha alterada com sucesso!")
        else:
            print("Login inexistente")
    elif opc == 4:
        login_excluir = input("Digite um login para excluir: ")
        if login_excluir in sistema_cadastro:
            sistema_cadastro.pop(login_excluir)
            print(f"Usuário {login_excluir} excluído com sucesso.")
        else:
            print("Login inexistente.")
    elif opc == 5:
        for c, v in sistema_cadastro.items():
            print(f"Login: {c}\nSenha: {v}")
            print("-"*20)
    elif opc == 6:
        print("Encerrando programa.")
        break
    else:
        print("Opção inválida. Digite outra opção.")