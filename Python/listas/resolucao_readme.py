# Resolução dos exercícios Readme.md

# Exercicio 1 
lista_compras = []
for i in range(5):
    item = input("Digite um item para a lista de compras: ")
    lista_compras.append(item)

print(f"Sua lista de compras: {lista_compras}")

# Exercicio 2
# Resolução 1 -
lista_numeros = []
maior_numero = float('-inf') # Menor valor possível
for i in range(5):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número digitado da lista {lista_numeros} foi: {maior_numero}")


# Resolução 2 -
lista_numeros = []
for i in range(5):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
maior_numero = max(lista_numeros)
print(f"O maior número digitado da lista {lista_numeros} foi: {maior_numero}")


# Exercicio 3
lista_numeros = []
qtd_pares = 0
qtd_impares = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1
print(f"Na lista {lista_numeros}, temos {qtd_pares} números pares e {qtd_impares} números ímpares.")


# Exercicio 4
# Resolução 1 -
qtd_numeros = int(input("Quantos números você quer digitar:  "))
lista_numeros = []
for i in range(qtd_numeros):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
total = 0
for num in lista_numeros:
    total += num
print(f"A soma dos números da lista {lista_numeros} é: {total}")

# Resolução 2 -
qtd_numeros = int(input("Quantos números você quer digitar:  "))
lista_numeros = []
for i in range(qtd_numeros):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
total = sum(lista_numeros)
print(f"A soma dos números da lista {lista_numeros} é: {total}")

# Resolução 3 -
qtd_numeros = int(input("Quantos números você quer digitar:  "))
lista_numeros = [float(input("Digite um número: ")) for _ in range(qtd_numeros)]
total = sum(lista_numeros)
print(f"A soma dos números da lista {lista_numeros} é: {total}")


# Exercicio 5
# Resolução 1 -
lista_numeros = []
for i in range(6):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
lista_sem_duplicados = []
for num in lista_numeros:
    if num not in lista_sem_duplicados:
        lista_sem_duplicados.append(num)
print(f"A lista sem números duplicados é: {lista_sem_duplicados}")

# Resolução 2 -
lista_numeros = []
for i in range(6):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
lista_sem_duplicados = list(set(lista_numeros))
print(f"A lista sem números duplicados é: {lista_sem_duplicados}")


# Exercício 6
lista_nomes = []
for i in range(4):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
nome_procurado = input("Digite o nome que deseja procurar: ")
if nome_procurado in lista_nomes:
    print(f"O nome {nome_procurado} foi encontrado na lista.")
else:
    print(f"O nome {nome_procurado} não foi encontrado na lista.")

# Exercício 7
lista_numeros = []
for i in range(5):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
lista_invertida = []
for i in range(len(lista_numeros)-1, -1, -1):
    lista_invertida.append(lista_numeros[i])
print(f"A lista invertida é: {lista_invertida}")

# Exercício 8
lista_numeros = []
lista_primos = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)
    if numero > 1:
        for j in range(2, int(numero**0.5) + 1):
            if numero % j == 0:
                break
        else:
            lista_primos.append(numero)
print(f"Os números primos da lista {lista_numeros} são: {lista_primos}")

# Exercício 9
lista_secreta = []
for i in range(5):
    numero = int(input("Digite números da lista secreta de 1 a 10: "))
    if 1 <= numero <= 10:
        lista_secreta.append(numero)
    print("Número inválido, digite um número entre 1 e 10.")
qtd_acertos = 0
for i in range(5):
    palpite = int(input("Tente adivinhar um número da lista secreta: "))
    if palpite in lista_secreta:
        print(f"Você acertou! O número {palpite} está na lista secreta.")
        qtd_acertos += 1
    else:
        print(f"Você errou. O número {palpite} não está na lista secreta.")
print(f"Você acertou {qtd_acertos} números da lista secreta {lista_secreta}.")

# Exercício 10
lista_notas = []
for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    lista_notas.append(nome)
    notas_aluno = []
    print(f"Digite as 5 notas do aluno {nome}:")
    for j in range(5):
        nota = float(input(f"Nota {j+1}: "))
        notas_aluno.append(nota)
    lista_notas.append(notas_aluno)
lista_media = []
print("Notas dos alunos:")
for i in range(0, len(lista_notas), 2):
    nome = lista_notas[i]
    notas = lista_notas[i+1]
    media = sum(notas) / len(notas)
    lista_media.append(media)
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    print(f"Aluno: {nome}, Notas: {notas}, Média: {media:.2f}, Situação: {situacao}")

media_turma = sum(lista_media) / len(lista_media)
print(f"Média da turma: {media_turma:.2f}")