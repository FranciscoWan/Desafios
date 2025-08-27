# 🐍 Lista de Desafios em Python - Laço `while` e Condicionais

Esta lista contém **12 desafios de programação** em Python, organizados do mais fácil ao mais difícil, utilizando apenas:

- Laço `while`
- Estruturas condicionais (`if`, `else`, `elif`)
- Palavras-chave `continue` e `break` em alguns exercícios

O objetivo é praticar lógica de repetição e controle de fluxo.

---

## 🚀 Desafios

### 1. Contagem simples
Peça para o usuário digitar um número `n` e faça a contagem de `1` até `n` usando `while`.

---

### 2. Contagem regressiva
Leia um número inteiro positivo e faça a contagem regressiva até chegar em `0`.

---

### 3. Somatória até zero
O programa deve ler números inteiros e somá-los até que o usuário digite `0`.

---

### 4. Número par ou ímpar (com `continue`)
Leia números do usuário até que ele digite `0`.  
- Se o número for **par**, exiba `"Par"`.  
- Se for **ímpar**, use `continue` para **pular a mensagem** e pedir outro número.

---

### 5. Adivinhe o número (com `break`)
Escolha um número secreto no código (ex: `7`).  
Peça para o usuário tentar adivinhar até ele acertar.  
- Se acertar → use `break` para encerrar.  
- Se errar → continue tentando.

---

### 6. Contagem de pares até limite
Peça para o usuário digitar um número `n`.  
Exiba apenas os números **pares** entre `1` e `n` usando `while`.

---

### 7. Validação de senha (com limite de tentativas)
Peça para o usuário digitar uma senha (predefinida no código, ex: `"python123"`).  
- O usuário tem no máximo **3 tentativas**.  
- Se acertar → mostre `"Acesso permitido"` e encerre com `break`.  
- Se errar todas → mostre `"Acesso negado"`.

---

### 8. Sequência até soma limite
Peça para o usuário digitar números.  
Continue somando até que o total ultrapasse `100`.  
Exiba quantos números foram digitados até passar do limite.

---

### 9. Números primos até N
Peça para o usuário um número `n`.  
Mostre todos os números **primos** até `n` usando apenas `while` e condicionais.

---

### 10. Menu interativo
Crie um programa que exiba um menu de opções em loop:

1- Dizer "Olá"  
2- Mostrar a tabuada de um número digitado pelo usuário  
3- Exibir todos os números de 1 a 20  
4- Sair  

Use `while True` para manter o menu rodando, `break` para sair, e `continue` se o usuário digitar uma opção inválida.

---

### 11. Mini caixa eletrônico
Simule um caixa eletrônico:  
- Usuário começa com saldo = 100  
- Exiba um menu com opções:  
  1- Depositar  
  2- Sacar  
  3- Ver saldo  
  4- Sair  

Regras:  
- Use `while True` e `break` para encerrar.  
- Se tentar sacar mais do que o saldo → mostrar mensagem de erro.  
- Se escolher opção inválida → use `continue`.

---

### 12. Jogo de adivinhação com níveis
Monte um jogo de adivinhação com dificuldade:  

- **Fácil** → número secreto entre 1 e 10  
- **Médio** → número secreto entre 1 e 50  
- **Difícil** → número secreto entre 1 e 100  

Regras:  
- A cada erro, o programa deve dar uma dica: `"O número é maior!"` ou `"O número é menor!"`.  
- O jogo termina quando:  
  - O usuário acerta (`break`)  
  - O usuário digita `0` para desistir  

---

📌 Agora é sua vez de praticar! Resolva os desafios em ordem e observe sua evolução na lógica de programação.  
