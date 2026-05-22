# 📊 Trade Analyzer

Sistema de análise financeira em Python para análise de operações com ações a partir de arquivos CSV, com persistência de dados via SQLite.

## 🚀 Objetivo

Transformar dados brutos de operações financeiras em insights claros e úteis, permitindo que o usuário consulte métricas da sua carteira de forma interativa através de um menu no terminal.

## 📂 Estrutura do Projeto
```
Trade-Analyzer/
│
├── main.py
├── vendas_acoes.csv
├── mercado.db (gerado automaticamente)
└── README.md

```

## 📥 Estrutura do CSV

O arquivo CSV deve conter as seguintes colunas:

| Coluna     | Tipo    | Exemplo         |
| ---------- | ------- | --------------- |
| Data       | TEXT    | 2026-01-02      |
| Ativo      | TEXT    | PETR4           |
| Preco      | REAL    | 30.00           |
| Quantidade | INTEGER | 100             |
| Tipo_Ordem | TEXT    | Compra ou Venda |

## ⚙️ Funcionalidades

### 📌 Leitura e Validação
- Input do nome do arquivo pelo usuário
- Tratamento de erros (arquivo não encontrado, vazio, inválido)
- Validação das colunas obrigatórias antes do processamento

### 📌 Banco de Dados (SQLite)
- Criação automática do banco `mercado.db`
- Persistência do histórico de operações entre sessões
- Proteção contra duplicatas — o mesmo CSV não é inserido duas vezes

### 📌 Métricas Calculadas
- Total investido e total resgatado da carteira
- Lucro/prejuízo total
- Lucro por ativo
- Retorno percentual por ativo
- Média de lucro/prejuízo
- Ativo que mais lucrou e que mais perdeu
- Total de ativos e operações na carteira

### 📌 Menu Interativo

[1] Visão geral da carteira
[2] Lucro por ativo
[3] Retorno percentual
[4] Analisar ativos vs valor alvo
[5] Mostrar tudo
[0] Sair

O menu permanece ativo até o usuário escolher sair.

### 📌 Insights por Ativo
Comparação do preço atual com o valor alvo definido:
- Acima do alvo → caro no momento
- Abaixo do alvo → possível oportunidade

## 🧠 Conceitos e Tecnologias Utilizados

- **Python** — lógica, funções, tratamento de erros
- **Pandas** — leitura de CSV, filtros booleanos, groupby, agregações
- **SQLite3** — criação de banco, inserção e consulta de dados
- **SQL** — CREATE TABLE, INSERT, SELECT, COUNT
- Estruturas de repetição e decisão
- Dicionários e f-strings formatadas

## 💻 Como Executar

1. Instale as dependências:
Nesse caso : pip install pandas

2. Prepare seu CSV com as colunas obrigatórias

3. Execute o programa:
python main.py


4. Digite o nome do arquivo CSV quando solicitado


## 🔮 Próximos passos 

* [ ] Consulta de histórico por ativo específico via SQL
* [ ] Separação do código em múltiplos arquivos
* [ ] Integração com yfinance para dados reais da B3
* [ ] Geração de relatório em .txt
* [ ] Gráfico de evolução de preço com matplotlib

## 🚧 Status

Projeto em desenvolvimento ativo — Fase 2 (SQLite) em andamento.

obs: Nesse momento estou implementando uma forma dos dados serem extraidos diretamente do SQLite 
e entendendo o processo de ETL atual, Extract : lê o CSV, Transform: Pandas calcula as métricas, 
Load: salva no banco

## 📌 Observações

Este projeto faz parte do meu processo de aprendizado em **Python para análise de dados**.
Ele será continuamente melhorado conforme avanço nos estudos.

## 👨‍💻 Autor

Pedro Augusto Silva Santos
