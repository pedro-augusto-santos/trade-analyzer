import pandas as pd
import sqlite3


def criar_banco():
    conn = sqlite3.connect("mercado.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data TEXT,
            Ativo TEXT,
            Preco REAL,
            Tipo_Ordem TEXT,
            Quantidade INTEGER,
            Valor_total REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precos_mercado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data TEXT,
            Ativo TEXT,
            Preco REAL,
            Volume REAL
        )
    """)

    conn.commit()
    conn.close()


def salvar_operacoes(df):
    conn = sqlite3.connect("mercado.db")
    df.to_sql("operacoes", conn, if_exists="append", index=False)
    conn.close()


def salvar_precos_mercado(df):
    conn = sqlite3.connect("mercado.db")
    df.to_sql("precos_mercado", conn, if_exists="append", index=False)
    conn.close()


def operacoes_vazias():
    conn = sqlite3.connect("mercado.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM operacoes")
    total = cursor.fetchone()[0]
    conn.close()
    return total == 0


def precos_vazios():
    conn = sqlite3.connect("mercado.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM precos_mercado")
    total = cursor.fetchone()[0]
    conn.close()
    return total == 0


def buscar_operacoes():
    conn = sqlite3.connect("mercado.db")
    df = pd.read_sql("SELECT * FROM operacoes", conn)
    conn.close()
    return df


def buscar_precos_mercado():
    conn = sqlite3.connect("mercado.db")
    df = pd.read_sql("SELECT * FROM precos_mercado", conn)
    conn.close()
    return df


def consultar_ativo(ativo):
    conn = sqlite3.connect("mercado.db")
    df = pd.read_sql(
        "SELECT * FROM precos_mercado WHERE Ativo = ?",
        conn,
        params=(ativo,)
    )
    conn.close()
    return df