# Desafios – Funções com *args e **kwargs

## Desafio 1 – Sistema de Pedidos Online
Crie uma função chamada `registrar_pedido(cliente, *produtos, **detalhes)` que:
- Receba o nome do cliente como argumento fixo.
- Utilize *args para os produtos pedidos.
- Utilize **kwargs para detalhes como forma de pagamento, endereço de entrega, cupom de desconto, etc.
A função deve exibir um resumo organizado do pedido.

---

## Desafio 2 – Cadastro de Funcionários
Crie uma função `cadastro_funcionario(nome, cargo, *competencias, **info_extra)` que:
- Receba nome e cargo como argumentos fixos.
- Receba várias competências usando *args.
- Receba informações adicionais como salário, setor e tempo de experiência com **kwargs.
A função deve exibir todos os dados formatados.

---

## Desafio 3 – Analisador de Dados
Crie uma função `analisar_dados(*valores, **opcoes)` que:
- Receba uma série de números usando *args.
- Receba opções como operação="media", operação="maior", operação="menor" usando **kwargs.
A função deve retornar o resultado da operação solicitada.

---

## Desafio 4 – Gerador de Relatórios Financeiros
Crie uma função `relatorio_financeiro(empresa, *valores, **config)` que:
- Receba o nome da empresa como argumento fixo.
- Receba os valores das receitas e despesas usando *args.
- Receba opções de configuração como moeda, exibir_media=True ou False, exibir_total=True ou False com **kwargs.
A função deve exibir um relatório financeiro formatado.

---

## Desafio 5 – Sistema de Eventos
Crie uma função `registrar_evento(nome_evento, *participantes, **detalhes)` que:
- Receba o nome do evento como argumento fixo.
- Utilize *args para os participantes do evento.
- Utilize **kwargs para informações adicionais como data, local e tema.
A função deve exibir os dados de forma clara para um relatório do evento.

---
