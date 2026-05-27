import pandas as pd
import sqlite3

def criar_banco():
    conn = sqlite3.connect("mercado.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data TEXT,
            Ativo TEXT,
            Preco REAL,
            Tipo_Ordem TEXT,
            Quantidade INTEGER,
            Valor_total REAL
        )
    """)
    
    conn.commit()
    conn.close()

def salvar_no_banco(df):
    conn = sqlite3.connect("mercado.db")
    df.to_sql("historico_precos", conn, if_exists = "append", index = False)
    conn.close()


def banco_vazio():
    conn = sqlite3.connect("mercado.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM historico_precos")
    total = cursor.fetchone()[0]
    conn.close()
    return total == 0


def buscar_do_banco():
    conn = sqlite3.connect("mercado.db")
    df = pd.read_sql("SELECT * FROM historico_precos",conn)
    conn.close()
    return df

def consultar_ativo(ativo):
    conn = sqlite3.connect("mercado.db")
    df = pd.read_sql("SELECT * FROM historico_precos WHERE Ativo = ?",conn, params = (ativo,))
    conn.close()
    return df
