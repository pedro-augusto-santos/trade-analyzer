import pandas as pd


def calcular_posicoes(df):
    compras = df[df["Tipo_Ordem"] == "Compra"].groupby("Ativo")["Quantidade"].sum()
    vendas = df[df["Tipo_Ordem"] == "Venda"].groupby("Ativo")["Quantidade"].sum()
    posicoes = (compras - vendas.reindex(compras.index, fill_value=0))
    posicoes = posicoes[posicoes > 0]
    return posicoes.to_dict()


def gerar_recomendacoes(df):
    recomendacoes = []

    for ativo in df["Ativo"].unique():
        historico = df[df["Ativo"] == ativo].sort_values("Data")

        if len(historico) < 2:
            continue

        preco_inicial = historico["Preco"].iloc[0]
        preco_atual = historico["Preco"].iloc[-1]
        variacao = ((preco_atual - preco_inicial) / preco_inicial) * 100

        if variacao > 5:
            recomendacao = "Manter"
        elif variacao < -5:
            recomendacao = "Atencao — queda relevante"
        else:
            recomendacao = "Neutro"

        recomendacoes.append(
            f"{ativo}: variacao de {variacao:.2f}% — Recomendacao: {recomendacao}"
        )

    return recomendacoes


def calcular_metricas_mercado(df):
    """Calcula metricas baseadas em precos de mercado via yfinance."""

    volatilidade = df.groupby("Ativo")["Preco"].std().fillna(0)
    qty_ativos = df["Ativo"].nunique()
    total_registros = len(df)

    preco_atual = df.sort_values("Data").groupby("Ativo")["Preco"].last()
    preco_inicial = df.sort_values("Data").groupby("Ativo")["Preco"].first()
    variacao = ((preco_atual - preco_inicial) / preco_inicial * 100).round(2)

    return {
        "qty_ativos": qty_ativos,
        "total_registros": total_registros,
        "volatilidade": volatilidade,
        "preco_atual": preco_atual,
        "variacao": variacao,
    }
