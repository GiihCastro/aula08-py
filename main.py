estoque = []

# Função para exibir a lista de produtos
def exibir_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    
    print(f"{'ID':<5} {'Nome':<25} {'Quantidade':<15} {'Preço':<15}")
    print("-" * 70)

    for produto in estoque:
        print(f"{produto['ID']:<5} {produto['Nome']:<25} {produto['Quantidade']:<15} {produto['Preço']:<15}")

# Função para remover um produto pelo ID
def remover_produto(estoque):
    try:
        id_produto = int(input("\nDigite o ID do produto que será removido: "))
        for produto_da_vez in estoque:
            if produto_da_vez["ID"] == id_produto:
                estoque.remove(produto_da_vez)
                print("Produto removido com sucesso!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Função para editar um produto
def editar_produto(estoque):
    try:
        id_produto = int(input("\nDigite o ID do produto que será removido: "))
        for produto_da_vez in estoque:
            if produto_da_vez["ID"] == id_produto:
              print("\nEscolha uma das opções abaixo:")
              menu = input('''\n ------ Editar produto ------
        | 1 - Editar nome do produto
        | 2 - Editar quantidade do produto
        | 3 - Editar preço do produto
        | 0 - Sair
        Digite sua escolha => ''')
              match menu:
                  case "1":
                      novo_nome = print("Digite o novo nome: ")
                      estoque[produto_da_vez]['Nome'] = novo_nome
                      print("Nome do produto alterado com sucesso!")
                  case "2":
                      nova_quantidade = print("Digite a nova quantidade: ")
                      estoque[produto_da_vez]['Quantidade'] = nova_quantidade
                      print("Quantidade do produto alterada com sucesso!")
                  case "3":
                      novo_preco = print("Digite o novo preço: ")
                      estoque[produto_da_vez]['Preço'] = novo_preco
                      print("Preço do produto alterado com sucesso!")
                  case "0":
                      print("Saindo do sistema...")
                      break
                  case _:
                      print("Opção inválida!")
        print("Produto não encontrado.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Sistema MyStock
while True:
    print('\nEscolha uma das opções abaixo:')
    menu = input('''\n ------ Sistema MyStock ------
        | 1 - Cadastrar produto
        | 2 - Exibir lista de produtos
        | 3 - Remover um produto
        | 4 - Editar um produto
        | 0 - Sair
            
        Digite sua escolha => ''')
    match menu:
        case "1":
            print("\n----- Cadastrar produto -----\n")
            nome = input("Digite o nome do produto: ")
            qtde = input("Digite a quantidade disponível desse produto no estoque: ")
            preco = input("Digite o preço do seu produto: ")

            produto = {
                "ID": len(estoque) + 1, 
                "Nome": nome,
                "Quantidade": qtde,
                "Preço": preco,
            }
            estoque.append(produto)

        case "2":
            print("\n----- Exibir lista de produtos -----\n")
            exibir_produtos(estoque)

        case "3":
            print("\n----- Remover um produto -----\n")
            exibir_produtos(estoque)
            remover_produto(estoque)

        case "4":
            print("\n----- Editar um produto -----\n")
            exibir_produtos(estoque)
            editar_produto(estoque)

        case "0":
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida!")