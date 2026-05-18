def menu():
    texto_menu = "MENU"
    print("=" * 30)
    print(f"{texto_menu.center(30)}")
    print("=" * 30)
    print("[1] Visão geral da carteira")
    print("[2] Lucro por ativo")
    print("[3] Retorno percentual")
    print("[4] Analisar ativos vs valor alvo")
    print("[5] Mostrar tudo")
    print("[0] Sair")
    

    while True:
        #Filtrando a String opção
        opcao = input("Por favor escolha uma opção").strip()
    
        if opcao in ["0", "1", "2", "3", "4", "5"]:
            #return tambem funciona como saída do loop
            return opcao
        else:
            print("Opção inválida. Digite um número entre 0 e 5.")

