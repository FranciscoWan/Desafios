# ========================================
# Desafio 1: O Maior de Dois Números
# ========================================
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print(f"O maior número é {a}")
elif b > a:
    print(f"O maior número é {b}")
else:
    print("Os números são iguais.")

# ========================================
# Desafio 2: Par ou Ímpar
# ========================================
n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")

# ========================================
# Desafio 3: A Porta Mágica
# ========================================
porta = int(input("Escolha uma porta (1, 2 ou 3): "))

if porta == 1:
    print("Você encontrou um tesouro!")
elif porta == 2:
    print("Você caiu em uma armadilha!")
elif porta == 3:
    print("Você encontrou a saída secreta!")
else:
    print("Porta inválida!")

# ========================================
# Desafio 4: Classificação Etária
# ========================================
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# ========================================
# Desafio 5: Calculadora Simples
# ========================================
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {n1 + n2}")
elif op == "-":
    print(f"Resultado: {n1 - n2}")
elif op == "*":
    print(f"Resultado: {n1 * n2}")
elif op == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Erro! Divisão por zero.")
else:
    print("Operação inválida.")

# ========================================
# Desafio 6: Triângulo Mágico
# ========================================
a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

if a == b == c:
    print("Triângulo Equilátero")
elif a == b or b == c or a == c:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")

# ========================================
# Desafio 7: A Prova Final
# ========================================
nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# ========================================
# Desafio 8: Ano Bissexto
# ========================================
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano comum")

# ========================================
# Desafio 9: O Cofre Secreto
# ========================================
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido! Cofre aberto.")
else:
    print("Acesso negado!")

# ========================================
# Desafio 10: O Jogo dos Números
# ========================================
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Maior e menor
maior = max(a, b, c)
menor = min(a, b, c)
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

# Progressão aritmética
if (b - a == c - b):
    print("Os números formam uma progressão aritmética!")
else:
    print("Os números NÃO formam uma progressão aritmética.")
