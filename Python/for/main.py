# Desafio 1 - O Lançamento de Foguetes da Agência Espacial
for i in range(10, 0, -1):
    print(i)
print("Fogo!!!")

# Desafio 2 - A Máquina de Tabuadas
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Desafio 3 - O Contador de Vogais
palavra = input("Digite uma palavra para saber quantas vogais existem nela: ")
cont = 0
for letra in palavra:
    if letra in ("a","e","i","o","u"):
        cont+=1
print(f"A palavra {palavra} possui {cont} vogais.")

# Desafio 4 - Somando as Compras do Supermercado
nItens = int(input("Digite o número de itens que comprou no mercado: "))
soma = 0
for i in range(nItens):
    preco = float(input(f"Valor do {nItens+1}° produto: "))
    soma += preco
print(f"A soma de {nItens} itens comprados no mercado foram de R$ {soma}.")

# Desafio 5 - Encontrando os Números Pares
intervalo = int(input("Digite o até qual números iremos mostrar os pares: "))
print(f"Os números pares no intervalo de 1 a {intervalo} são:")
for i in range(1, intervalo+1):
    if i%2==0:
        print(i, end=" ")
print("\n")

# Desafio 6 - O Robô de Limpeza
largura = int(input("Digite a largura da sala: "))
altura = int(input("Digite a altura da sala: "))
area = largura*altura
for i in range(1, area+1):
    print(f"O robô limpou {i} metros.")
print("Limpeza finalizada.")

# Desafio 7 - O Alfabeto ao Contrário
alfabeto = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alfabetoTratado = alfabeto.replace(", ", "")[::-1]
for letra in alfabetoTratado:
    print(letra)

# Desafio 8 - Montando a Pirâmide de Blocos
nAndares = int(input("Digite o tamanho da pirâmide que deseja construir: "))
for i in range(1, nAndares+1):
    print("*"*i)

# Desafio 9 - A Fábrica de Biscoitos
qtdBiscoitoHora = int(input("Digite a quantia de biscoitos produzidos por hora: "))
turno = int(input("Digite o número de horas do turno: "))
totalBiscoitos = 0
for i in range(turno):
    totalBiscoitos += qtdBiscoitoHora
    print(f"Foram produzidos {totalBiscoitos} até agora.")
print(f"O total de biscoitos produzidos foi de {totalBiscoitos}")

# Desafio 10 - O Atleta em Treinamento
distAtual = int(input("Digite a distância inicial de treino: "))
for i in range(1,8):
    print(f"Distância para percorrer do dia {i} - {distAtual:.2f} km.")
    distAtual *= 1.10

# Desafio FINAL - O Mapa do Tesouro
for linha in range(1,6):
    for coluna in range(1,6):
        if linha == 3 and coluna == 4:
            print(" x ", end="")
        else:
            print(" . ", end="")
    print()