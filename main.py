import pandas as pd

texto = "TRADE ANALYZER"

print("=" * 50)
print(f"{texto.center(50)}")
print("=" * 50)


# --- INÍCIO DO PROGRAMA ---
def carregar_dados():
    arquivo = input("Nome do arquivo CSV (ex: vendas_acoes.csv): ").strip()
    
    df = None

    try:
        df = pd.read_csv(arquivo, sep=",")

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o nome ou o caminho")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio")
    except pd.errors.ParserError:
        print("Erro: Problemas na estrutura do CSV")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return df


def calcular_metricas(df):
    """Calcula compras, vendas, lucro e média."""

    print(df.head())
    print("\n")

    # Cria uma nova coluna que mostra quanto dinheiro foi movimentado por operação
    df["Valor_total"] = df["Quantidade"] * df["Preco"]

    # Filtro booleano: TRUE --> mantém linha | FALSE --> remove linha
    # Agrupa os ativos e soma o valor total de cada grupo
    compras = df[df["Tipo_Ordem"] == "Compra"].groupby("Ativo")["Valor_total"].sum()
    vendas = df[df["Tipo_Ordem"] == "Venda"].groupby("Ativo")["Valor_total"].sum()

    resultado = vendas - compras
    retorno_percentual = ((vendas - compras) / compras) * 100

    # .fillna(0) troca valores vazios por 0 e .mean() calcula a média
    media = resultado.fillna(0).mean()

    print("Compras:\n", compras)
    print("\nVendas:\n", vendas)
    print("\nLucros por ativo:\n", resultado)
    print("\nRetorno percentual por ativo:\n",retorno_percentual)
    print("\nMédia de lucro/prejuízo:", media)
    print()

    return resultado, media


def menu():
    """Verifica se o usuário quer ou não continuar."""

    while True:
        insights = input("Deseja obter mais análises? (s/n): ").lower().strip()

        if insights in ["s", "n"]:
            break
        else:
            print("Resposta inválida. Digite s ou n.")
            print()

    return insights

def gerar_insights(df, valores_alvo):
    """Analisa cada ativo e compara com o valor alvo."""

    for ativo in df["Ativo"].unique():
        preco_atual = df[df["Ativo"] == ativo]["Preco"].iloc[-1]

        print(f"\nAnalisando {ativo}...")
        print(f"Preço atual: R$ {preco_atual:.2f}")

        alvo = valores_alvo.get(ativo)

        if alvo is None:
            print(f"{ativo}: Valor alvo não cadastrado")
            continue

        print(f"Valor alvo: R$ {alvo:.2f}")

        # Decisão:
        # Acima do alvo == caro
        # Abaixo do alvo == barato
        if preco_atual > alvo:
            print("Acima do valor alvo (caro no momento)")
        elif preco_atual < alvo:
            print("Abaixo do valor alvo (possível oportunidade)")
        else:
            print("No valor exato do alvo")

def main():

    valores_alvo = {
    "PETR4": 38,
    "VALE3": 78,
    "ITUB4": 29,
    "BBDC4": 50,
    "ABEV3": 12
    }
    

    df = carregar_dados()

    if df is not None:
        calcular_metricas(df)

        opcao = menu()

        if opcao == "s":
            gerar_insights(df,valores_alvo)
        else:
            print("Programa encerrado.")


main()