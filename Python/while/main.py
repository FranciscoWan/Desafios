# Atividade 1 -
n = int(input("Digite um número: "))
i = 1
while i <= n:
    print(i)
    i += 1

# Atividade 2 - 
n = int(input("Digite um número: "))
while n >= 0:
    print(n)
    n -= 1

# Atividade 3 - 
soma = 0
num = int(input("Digite um número (0 para parar): "))

while num != 0:
    soma += num
    num = int(input("Digite um número (0 para parar): "))

print(f"Soma final: {soma}.")

# Atividade 4 -
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    if num % 2 != 0:
        continue
    print("Par")

# Atividade 5 - 
segredo = 7

while True:
    chute = int(input("Adivinhe o número (0 para sair): "))
    if chute == 0:
        print("Você desistiu!")
        break
    if chute == segredo:
        print("Parabéns, você acertou!")
        break
    else:
        print("Tente novamente!")

# Atividade 6 - 
n = int(input("Digite um número: "))
i = 1

while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

# Atividade 7 -
senha_correta = "python123"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta!")
    tentativas += 1

if tentativas == 3 and senha != senha_correta:
    print("Acesso negado!")

# Atividade 8 -
soma = 0
contador = 0

while soma <= 100:
    num = int(input("Digite um número: "))
    soma += num
    contador += 1

print(f"Você digitou {contador} números e a soma foi de: {soma}")

# Atividade 9 -
num = int(input("Deseja ver os números primos até qual número? "))
cont = 2  # começa do 2, já que 1 não é primo

while cont <= num:
    divisores = 0
    inicio = 1
    
    while inicio <= cont:
        if cont % inicio == 0:
            divisores += 1
        inicio += 1

    if divisores == 2:
        print(f"O número {cont} é primo.")
    
    cont += 1

# Atividade 10 - 
while True:
    print("\n--- MENU ---")
    print("1 - Dizer Olá")
    print("2 - Tabuada")
    print("3 - Números de 1 a 20")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá!")
    elif opcao == "2":
        n = int(input("Digite um número: "))
        i = 1
        while i <= 10:
            print(f"{n} x {i} = {n*i}")
            i += 1
    elif opcao == "3":
        i = 1
        while i <= 20:
            print(i, end=" ")
            i += 1
        print()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
        continue

# Atividade 11 -
saldo = 100

while True:
    print("\n--- CAIXA ELETRÔNICO ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print("Depósito realizado!")
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            print("Saque realizado!")
    elif opcao == "3":
        print("Saldo atual:", saldo)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        continue

# Atividade 12 - 
import random

print("--- Jogo da Adivinhação ---")
print("Escolha a dificuldade:")
print("1 - Fácil (1 a 10)")
print("2 - Médio (1 a 50)")
print("3 - Difícil (1 a 100)")

nivel = int(input("Digite o nível: "))

if nivel == 1:
    limite = 10
elif nivel == 2:
    limite = 50
else:
    limite = 100

segredo = random.randint(1, limite)

while True:
    chute = int(input("Digite seu palpite (0 para desistir): "))

    if chute == 0:
        print("Você desistiu!")
        break

    if chute == segredo:
        print("Parabéns! Você acertou!")
        break
    elif chute < segredo:
        print("O número é maior!")
    else:
        print("O número é menor!")
