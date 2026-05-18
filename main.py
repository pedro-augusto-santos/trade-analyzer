import pandas as pd

texto = "TRADE ANALYZER"

print()
print("=" * 50)
print(f"{texto.center(50)}")
print("=" * 50)
print()


# --- INÍCIO DO PROGRAMA ---
def carregar_dados():
    arquivo = input("Nome do arquivo CSV (ex: vendas_acoes.csv): ").strip()
    print()
    
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

def menu():
    texto_menu = "MENU"
    print("=" * 30)
    print(f"{texto_menu.center(30)}")
    print("=" * 30)
    print()
    print("[1] Visão geral da carteira")
    print("[2] Lucro por ativo")
    print("[3] Retorno percentual")
    print("[4] Analisar ativos vs valor alvo")
    print("[5] Mostrar tudo")
    print("[0] Sair")
    print()
    

    while True:
        #Filtrando a String opção
        opcao = input("Por favor escolha uma opção: ").strip()
    
        if opcao in ["0", "1", "2", "3", "4", "5"]:
            #return tambem funciona como saída do loop
            return opcao
        else:
            print("Opção inválida. Digite um número entre 0 e 5.")

def gerar_insights(opcao, metricas, valores_alvo, df):

    if opcao == "1":
        print(f"Total investido: R$ {metricas['tot_investido']:.2f}")
        print(f"Total resgatado: R$ {metricas['tot_resgatado']:.2f}")
        print(f"Lucro total: R$ {metricas['lucro_total']:.2f}")
        print(f"Média de lucro: R$ {metricas['media']:.2f}")
        print(f"Ativos na carteira: {metricas['qty_ativos']}")
        print(f"Total de operações: {metricas['total_operacoes']}")

    elif opcao == "2":
        #Lucro por ativo
        print(f"Ativo que mais lucrou: {metricas['ativo_mais_lucrou']}")
        print(f"Ativo que mais perdeu: {metricas['ativo_menos_lucrou']}")
        print(f"Lucro total da carteira: R$ {metricas['lucro_total']:.2f}")
       

    
    elif opcao == "3":
        #Retorno Percentual
        print(f"Retorno percentual:{metricas['retorno_percentual']}")
        
    elif opcao == "4":
        #Analisa ativo vs valor alvo
        for ativo in df["Ativo"].unique():
            #Percorre cada ativo único do CSV e ignora repetidos.

            preco_atual = df[df["Ativo"] == ativo]["Preco"].iloc[-1]
            #filtra o DataFrame, mantém só as linhas daquele ativo. pega só a coluna Preço dessas linhas, e pega o último elemento.

            alvo = valores_alvo.get(ativo)
            #Busca a chave ativo ddentro do dicionário

            print(f"\n{ativo}")
            print(f"Preço atual: R$ {preco_atual:.2f}")

            if alvo is None:
                print("Valor alvo não cadastrado")
                continue

            print(f"Valor alvo: R$ {alvo:.2f}")  # ← dentro do for

            if preco_atual > alvo:              # ← dentro do for
                print("Acima do valor alvo (caro no momento)")
            elif preco_atual < alvo:
                print("Abaixo do valor alvo (possível oportunidade)")
            else:
                print("No valor exato do alvo")

    elif opcao == "5":
        #Retorna tudo
        print(f"\nTotal investido: R$ {metricas['tot_investido']:.2f}")
        print(f"Total resgatado: R$ {metricas['tot_resgatado']:.2f}")
        print(f"Lucro total: R$ {metricas['lucro_total']:.2f}")
        print(f"Média de lucro: R$ {metricas['media']:.2f}")
        print(f"Ativos na carteira: {metricas['qty_ativos']}")
        print(f"Total de operações: {metricas['total_operacoes']}")
        print(f"\nAtivo que mais lucrou: {metricas['ativo_mais_lucrou']}")
        print(f"Ativo que mais perdeu: {metricas['ativo_menos_lucrou']}")
        print(f"\nRetorno percentual por ativo:\n{metricas['retorno_percentual']}")


    elif opcao == "0":
        print("Encerrando...")
        return

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
        metricas = calcular_metricas(df)
        opcao = menu()
        gerar_insights(opcao, metricas, valores_alvo, df)
    
main()
