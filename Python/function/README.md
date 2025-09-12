# Desafios de Funções I em Python

Este documento contém 10 desafios que utilizam funções em conjunto com os conteúdos já estudados:  
- Variáveis e operadores  
- Condicionais (`if`, `elif`, `else`)  
- Laços de repetição (`for`, `while`)  
- Listas, tuplas, dicionários e sets  
- Funções  

---

## Desafio 1  
Crie uma função chamada `soma_lista` que receba uma lista de números e retorne a soma de todos os elementos.  

---

## Desafio 2  
Crie uma função chamada `maior_menor` que receba uma lista de números e retorne o maior e o menor valor encontrados.  

---

## Desafio 3  
Crie uma função chamada `contar_palavras` que receba uma string e retorne a quantidade de palavras nela.  

---

## Desafio 4  
Crie uma função chamada `cadastro_alunos` que receba um dicionário vazio.  
A função deve permitir adicionar alunos com nome e nota em diferentes matérias.  

---

## Desafio 5  
Crie uma função chamada `busca_aluno` que receba o dicionário do desafio anterior e um nome de aluno.  
A função deve retornar as notas do aluno informado.  

---

## Desafio 6  
Crie uma função chamada `conjunto_unico` que receba uma lista com números repetidos e retorne um set com apenas os valores únicos.  

---

## Desafio 7  
Crie uma função chamada `verificar_login` que receba um dicionário de usuários e senhas e um par usuário/senha como parâmetros.  
A função deve retornar **True** se o login for válido e **False** caso contrário.  

---

## Desafio 8  
Crie uma função chamada `tabuada_intervalo` que receba um número e um limite.  
A função deve imprimir a tabuada do número até o limite informado.  

---

## Desafio 9  
Crie uma função chamada `estatisticas_notas` que receba uma lista de notas e retorne:  
- média das notas  
- maior nota  
- menor nota  

---

## Desafio 10  
Crie uma função chamada `sistema_cadastro` que permita:  
- adicionar alunos (nome e notas)  
- calcular média de cada aluno  
- exibir todos os alunos cadastrados e suas situações (aprovado/reprovado).  

---

## Desafio 11  

Crie um sistema completo de **gerenciamento de turma** utilizando **funções**, **listas**, **dicionários**, **sets** e estruturas de controle.  

O sistema deve permitir:  
1. **Cadastrar alunos** com nome, idade e notas em diferentes matérias.  
2. **Evitar cadastros duplicados** (use um `set` para garantir nomes únicos).  
3. **Remover alunos** pelo nome.  
4. **Exibir todos os alunos cadastrados**, mostrando suas notas, média e situação (aprovado/reprovado).  
5. **Exibir estatísticas gerais da turma**, como:  
   - número total de alunos  
   - maior média  
   - menor média  
   - média geral da turma  
6. **Buscar um aluno específico** pelo nome e mostrar suas informações.  
7. **Sair do programa** apenas quando o usuário escolher a opção correspondente.  

> Dica: use funções separadas para cada funcionalidade (ex.: `adicionar_aluno()`, `remover_aluno()`, `estatisticas_turma()`) e organize bem o código.  
