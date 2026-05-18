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
