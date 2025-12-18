# Desafio 1:
## Desafio: Sistema de Login com Persistência de Dados

## Contexto

Uma pequena empresa está desenvolvendo um sistema simples de autenticação para controlar o acesso de usuários ao seu sistema interno. Como o sistema ainda está em fase inicial, decidiu-se implementar uma solução em Python, utilizando arquivos locais para armazenar as credenciais de acesso.

O sistema deve permitir a criação de um usuário na primeira execução e, nas execuções seguintes, validar o login com base nas informações previamente salvas. Para aumentar a segurança e a usabilidade, o sistema também contará com limite de tentativas e uma dica de senha.

## Objetivo

Desenvolver um programa em Python que:

- Cadastre credenciais de acesso (login, senha e dica) caso ainda não existam.
- Armazene essas credenciais em um arquivo no formato JSON.
- Permita que o usuário tente acessar o sistema utilizando login e senha.
- Controle o número de tentativas de acesso.
- Exiba mensagens claras de sucesso, erro ou bloqueio do sistema.

## Requisitos Funcionais

### 1. Cadastro Inicial

Caso o arquivo de credenciais não exista, o sistema deve:

- Solicitar ao usuário um nome de login.
- Solicitar uma senha.
- Solicitar uma dica para recuperação da senha.
- Salvar essas informações em um arquivo `credenciais.json`.

### 2. Menu Inicial

Caso o arquivo já exista, o sistema deve exibir um menu com as opções:

- `1 - Entrar`
- `2 - Sair`

### 3. Processo de Login

Ao escolher a opção de entrar:

- Exibir uma animação simples de carregamento.
- Solicitar login e senha.
- Comparar os dados informados com os dados armazenados.
- Permitir até 3 tentativas de acesso.

### 4. Validação e Segurança

- Se o login e a senha estiverem corretos, exibir uma mensagem de boas-vindas.
- Se ambos estiverem incorretos:
  - Reduzir o número de tentativas.
  - Na segunda tentativa incorreta, exibir a dica da senha.
  - Encerrar o programa ao esgotar as tentativas.
- Se apenas um dos dados estiver incorreto, encerrar o programa imediatamente por segurança.

### 5. Encerramento

O sistema deve permitir a saída segura quando o usuário escolher a opção correspondente ou quando o número de tentativas for excedido.

## Regras e Observações

- Utilize os módulos `json`, `os` e `time`.
- O arquivo de credenciais deve ser salvo no mesmo diretório do programa.
- As mensagens exibidas devem ser claras e amigáveis ao usuário.
- O foco do desafio é praticar:
  - Manipulação de arquivos
  - Estruturas condicionais
  - Laços de repetição
  - Controle de fluxo
  - Simulação de sistemas reais simples

## Dicas de Implementação

1. Use `os.path.exists()` para verificar se o arquivo de credenciais já existe.
2. Use `json.dump()` para salvar e `json.load()` para ler as credenciais.
3. Implemente a animação de carregamento com `time.sleep()` e caracteres especiais.
4. Utilize variáveis de controle para gerenciar o número de tentativas.
5. Estruture seu código com funções para melhor organização.

## Exemplo de Estrutura do JSON

```json
{
  "login": "usuario123",
  "senha": "senha_secreta",
  "dica": "Nome do meu pet"
}
```

**Boa sorte e bom código! 🚀**
