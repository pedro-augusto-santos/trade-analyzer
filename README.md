# 📊 Trade Analyzer

Projeto em Python utilizando **Pandas** para análise de operações com ações a partir de um arquivo CSV.

---

## 🚀 Objetivo

Transformar dados brutos de operações financeiras em **insights claros e úteis**, como:

* Total investido por ativo
* Total vendido por ativo
* Lucro ou prejuízo
* Média geral de desempenho
* Análise de preço atual vs valor alvo

---

## 📂 Estrutura do Projeto

```
Trade-Analyzer/
│
├── main.py
├── vendas_acoes.csv
└── README.md
```

---

## 📥 Estrutura do CSV

O arquivo `vendas_acoes.csv` deve conter as seguintes colunas:

* `Data`
* `Ativo`
* `Preco`
* `Quantidade`
* `Tipo_Ordem` (Compra ou Venda)

---

## ⚙️ Funcionalidades

### 📌 Leitura e validação

* Tratamento de erros (arquivo não encontrado, vazio ou inválido)

### 📌 Processamento

* Criação da coluna `Valor_total`
* Separação de compras e vendas
* Agrupamento por ativo (`groupby`)
* Cálculo de lucro/prejuízo

### 📌 Análises

* Exibição de:

  * Compras totais
  * Vendas totais
  * Resultado por ativo
  * Média geral

### 📌 Insights interativos

* Análise de preço atual vs valor alvo
* Classificação:

  * Acima do alvo → caro
  * Abaixo do alvo → oportunidade

---

## 🧠 Conceitos utilizados

* Pandas (`DataFrame`)
* Agregações (mean(),sum())
* Multiplicação de colunas
* Filtro booleano
* `groupby`
* Operações entre colunas
* Tratamento de exceções (`try/except`)
* Estruturas de repetição e decisão

---

## 🚧 Status do Projeto

Projeto em desenvolvimento 🚧

Atualmente pausado para aprofundamento em **Pandas**, com foco em:

* Manipulação de dados
* Filtros
* Agrupamentos

Retorno previsto com melhorias e refatoração do código.

---

## 🔮 Próximos passos 

* [ ] Melhorar organização do código (funções)
* [ ] Adicionar validações
* [ ] Aprimorar análises de lucro/prejuízo
* [ ] Criar novas métricas
* [ ] Implementar visualizações

---

## 💻 Como executar

1. Instale as dependências:

```
pip install pandas
```

2. Execute o programa:

```
python main.py
```

---

## 📌 Observações

Este projeto faz parte do meu processo de aprendizado em **Python para análise de dados**.
Ele será continuamente melhorado conforme avanço nos estudos.

---

## 👨‍💻 Autor

Pedro Augusto Silva Santos
