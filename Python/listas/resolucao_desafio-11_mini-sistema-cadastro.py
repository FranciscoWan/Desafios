lista_alunos = []
while True:
    print("\n--- Menu ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Buscar aluno pelo nome")
    print("4 - Mostrar média geral da turma")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        aluno = []
        nome = input("Nome do aluno: ")
        aluno.append(nome)
        notas = []
        for i in range(1, 4):
            nota = float(input(f"Nota {i}: "))
            notas.append(nota)
        aluno.append(notas)
        lista_alunos.append(aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")

    elif opcao == '2':
        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n--- Lista de Alunos ---")
            for aluno in lista_alunos:
                nome = aluno[0]
                notas = aluno[1]
                media = sum(notas) / len(notas)
                print(f"Nome: {nome}, Notas: {notas}, Média: {media:.2f}")
    
    elif opcao == '3':
        nome_busca = input("Digite o nome do aluno para buscar: ")
        encontrado = False
        for aluno in lista_alunos:
            if aluno[0].lower() == nome_busca.lower():
                notas = aluno[1]
                media = sum(notas) / len(notas)
                print(f"Nome: {aluno[0]}, Notas: {notas}, Média: {media:.2f}")
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")
    
    elif opcao == '4':
        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            soma_medias = 0
            for aluno in lista_alunos:
                notas = aluno[1]
                media = sum(notas) / len(notas)
                soma_medias += media
            media_geral = soma_medias / len(lista_alunos)
            print(f"Média geral da turma: {media_geral:.2f}")
    
    elif opcao == '5':
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")