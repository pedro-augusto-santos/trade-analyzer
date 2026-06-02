import yfinance as yf
import pandas as pd
import sqlite3
from database import salvar_precos_mercado


def buscar_historico(ativo, periodo="6mo"):
    ticker = yf.Ticker(f"{ativo}.SA")
    historico = ticker.history(period=periodo)

    if historico.empty:
        print(f"{ativo}: nao encontrado na API.")
        return None

    df = historico.reset_index()[["Date", "Close", "Volume"]]
    df.columns = ["Data", "Preco", "Volume"]
    df["Ativo"] = ativo
    df["Data"] = df["Data"].dt.strftime("%Y-%m-%d")

    return df


def filtrar_novos_registros(df, ativo):
    conn = sqlite3.connect("mercado.db")
    datas_existentes = pd.read_sql(
        "SELECT Data FROM precos_mercado WHERE Ativo = ?",
        conn,
        params=(ativo,)
    )["Data"].tolist()
    conn.close()
    return df[~df["Data"].isin(datas_existentes)]


def atualizar_precos():
    ativos = ["PETR4", "VALE3", "ITUB4", "BBDC4", "ABEV3"]

    for ativo in ativos:
        print(f"Buscando {ativo}...")
        df = buscar_historico(ativo)

        if df is not None:
            df = filtrar_novos_registros(df, ativo)
            if df.empty:
                print(f"{ativo}: nenhum registro novo.")
            else:
                salvar_precos_mercado(df)
                print(f"{ativo}: {len(df)} registros novos salvos.")

