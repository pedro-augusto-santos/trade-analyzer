import pandas as pd

texto = "TRADE ANALYZER"

print("=" * 50)
print(f"{texto.center(50)}")
print("=" * 50)


# --- INÍCIO DO PROGRAMA ---
def carregar_dados():
    """Lê o CSV e retorna o dataframe. Se der erro, retorna None."""

    # df começa vazio para caso tenha erro no arquivo o programa não quebre
    df = None

    try:
        df = pd.read_csv("vendas_acoes.csv", sep=",")

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

    # .fillna(0) troca valores vazios por 0 e .mean() calcula a média
    media = resultado.fillna(0).mean()

    print("Compras:\n", compras)
    print("\nVendas:\n", vendas)
    print("\nLucros por ativo:\n", resultado)
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


def gerar_insights(df, valor_alvo=35):
    """Analisa cada ativo e compara com o valor alvo."""

    for ativo in df["Ativo"].unique():
        # Pega todos os ativos únicos e o último preço de cada um
        preco_atual = df[df["Ativo"] == ativo]["Preco"].iloc[-1]

        print(f"\nAnalisando {ativo}...")
        print(f"Preço atual: {preco_atual}")
        print(f"Valor alvo: {valor_alvo}")

        # Decisão:
        # Acima do alvo == caro
        # Abaixo do alvo == barato
        if preco_atual > valor_alvo:
            print("Acima do valor alvo (caro no momento)")
        elif preco_atual < valor_alvo:
            print("Abaixo do valor alvo (possível oportunidade)")
        else:
            print("No valor exato do alvo")


def main():
    df = carregar_dados()

    if df is not None:
        calcular_metricas(df)

        opcao = menu()

        if opcao == "s":
            gerar_insights(df)
        else:
            print("Programa encerrado.")


main()