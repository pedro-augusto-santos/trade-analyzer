def calcular_metricas(df):
    """Calcula compras, vendas, lucro e média..."""


    # Cria uma nova coluna que mostra quanto dinheiro foi movimentado por operação
    df["Valor_total"] = df["Quantidade"] * df["Preco"]

    # Filtro booleano: TRUE --> mantém linha | FALSE --> remove linha
    # Agrupa os ativos e soma o valor total de cada grupo
    compras = df[df["Tipo_Ordem"] == "Compra"].groupby("Ativo")["Valor_total"].sum()

    vendas = df[df["Tipo_Ordem"] == "Venda"].groupby("Ativo")["Valor_total"].sum()

    tot_investido = df[df["Tipo_Ordem"] == "Compra"]["Valor_total"].sum()

    tot_resgatado = df[df["Tipo_Ordem"] == "Venda"]["Valor_total"].sum()

    #Lucro por ativo
    lucro_ativo = vendas - compras

    ativo_mais_lucrou = lucro_ativo.idxmax()

    ativo_menos_lucrou = lucro_ativo.idxmin()
    
    #Lucro total da carteira
    lucro_tot = lucro_ativo.sum()

    retorno_percentual = ((vendas - compras) / compras) * 100

    qty_ativos = df["Ativo"].nunique()

    total_de_operacoes = len(df)

    # .fillna(0) troca valores vazios por 0 e .mean() calcula a média
    media = lucro_ativo.fillna(0).mean()

    return {
    "tot_investido": tot_investido,
    "tot_resgatado": tot_resgatado,
    "media": media,
    "total_operacoes": total_de_operacoes,
    "qty_ativos": qty_ativos,
    "retorno_percentual": retorno_percentual,
    "lucro_total": lucro_tot,
    "ativo_menos_lucrou": ativo_menos_lucrou,
    "ativo_mais_lucrou": ativo_mais_lucrou,
}
