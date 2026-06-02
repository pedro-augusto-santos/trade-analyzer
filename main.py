# main.py
import pandas as pd
from time import sleep
from database import criar_banco, salvar_operacoes, operacoes_vazias, precos_vazios, buscar_operacoes, buscar_precos_mercado, consultar_ativo
from analise import calcular_metricas_mercado, gerar_recomendacoes
from yfinance_api import atualizar_precos

texto = "TRADE ANALYZER"

print()
print("=" * 50)
print(f"{texto.center(50)}")
print("=" * 50)
print()


def carregar_dados():
    arquivo = input("Nome do arquivo CSV (ex: vendas_acoes.csv): ").strip()
    print()

    df = None

    try:
        df = pd.read_csv(arquivo, sep=",")
        print("Carregando dados...")
        sleep(1)
        print("Dados carregados com sucesso!")
        sleep(0.5)
        print()

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o nome ou o caminho")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio")
    except pd.errors.ParserError:
        print("Erro: Problemas na estrutura do CSV")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return df


def validar_colunas(df):
    colunas_esperadas = {"Data", "Ativo", "Preco", "Tipo_Ordem", "Quantidade"}
    colunas_faltando = colunas_esperadas - set(df.columns)

    if colunas_faltando:
        print(f"Erro: CSV inválido. Colunas faltando: {colunas_faltando}")
        return False

    return True


def menu():
    texto_menu = "MENU"
    print("=" * 30)
    print(f"{texto_menu.center(30)}")
    print("=" * 30)
    print()
    print("[1] Visão geral da carteira")
    print("[2] Lucro por ativo")
    print("[3] Retorno percentual")
    print("[4] Posições abertas")
    print("[5] Volatilidade dos ativos")
    print("[6] Consultar ativo específico")
    print("[7] Atualizar preços via API")
    print("[8] Recomendações automáticas")
    print("[0] Sair")
    print()

    while True:
        opcao = input("Por favor escolha uma opção: ").strip()

        if opcao in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            return opcao
        else:
            print("Opção inválida. Digite um número entre 0 e 8.")


def gerar_insights(opcao, metricas, dfsql):

    print("-" * 30)

    if opcao == "1":
        print(f"Ativos monitorados: {metricas['qty_ativos']}")
        print(f"Total de registros: {metricas['total_registros']}")
        print(f"\nPreço atual por ativo:\n{metricas['preco_atual'].to_string()}")
        print(f"\nVariação total por ativo (%):\n{metricas['variacao'].to_string()}")

    elif opcao == "2":
        print(f"Variação por ativo (%):\n{metricas['variacao'].to_string()}")

    elif opcao == "3":
        print(f"Variação percentual por ativo:\n{metricas['variacao'].to_string()}")

    elif opcao == "4":
        print("Posições abertas disponíveis apenas com operações pessoais importadas.")

    elif opcao == "5":
        print("Volatilidade por ativo:\n")
        print(metricas["volatilidade"].to_string())

    elif opcao == "8":
        recomendacoes = gerar_recomendacoes(dfsql)
        for linha in recomendacoes:
            print(linha)

    print()

def main():

    valores_alvo = {
        "PETR4": 38,
        "VALE3": 78,
        "ITUB4": 29,
        "BBDC4": 50,
        "ABEV3": 12
    }

    criar_banco()

    if operacoes_vazias():
        df = carregar_dados()
        if df is not None:
            if not validar_colunas(df):
                print("Corrija o CSV e tente novamente.")
                return
            df["Valor_total"] = df["Quantidade"] * df["Preco"]
            salvar_operacoes(df)
        else:
            print("Não foi possível carregar o arquivo. Encerrando.")
            return

    if precos_vazios():
        print("Buscando dados reais da B3...")
        sleep(1)
        atualizar_precos()

    dfsql = buscar_precos_mercado()
    metricas = calcular_metricas_mercado(dfsql)

    while True:
        opcao = menu()

        if opcao == "0":
            print("Encerrando...")
            sleep(2)
            break

        elif opcao == "6":
            ativo = input("Digite o ticker do ativo: ").strip().upper()
            resultado = consultar_ativo(ativo)
            if resultado.empty:
                print("Ativo não encontrado no banco")
            else:
                print(resultado)

        elif opcao == "7":
            print("Buscando preços atualizados...")
            atualizar_precos()
            dfsql = buscar_precos_mercado()
            metricas = calcular_metricas_mercado(dfsql)
            print("Preços atualizados com sucesso!")

        else:
            gerar_insights(opcao, metricas, dfsql)


main()