produtos = [
    {
        "id_produto": 1,
        "id_fornecedor": 1,
        "id_localizacao": 1,
        "id_categoria": 1,
        "id_marca": 1,
        "nome_produto": "Exemplo Produto",
        "descricao": "Descrição do produto de exemplo",
        "preco": 10.0,
        "quantidade_estoque": 5,
        "imagem_url": "http://mercado.com/imagem.jpg"
    }
]

def atualizar_produto(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    try:
        id_busca = int(input("Digite o ID do produto que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    produto = next((p for p in produtos if p["id_produto"] == id_busca), None)
    if not produto:
        print(f"Produto com ID {id_busca} não encontrado.")
        return

    print("\nProduto encontrado:")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

    print("\nDigite os novos valores (deixe vazio para não alterar):")

    novo_nome = input("Novo nome do produto: ").strip()
    if novo_nome:
        if 1 <= len(novo_nome) <= 150:
            produto["nome_produto"] = novo_nome
        else:
            print("Nome inválido, não alterado.")

    nova_descricao = input("Nova descrição do produto: ").strip()
    if nova_descricao:
        produto["descricao"] = nova_descricao[:500]

    novo_preco = input("Novo preço do produto: ").replace(",", ".").strip()
    if novo_preco:
        try:
            preco_float = float(novo_preco)
            if preco_float >= 0:
                produto["preco"] = preco_float
            else:
                print("Preço negativo, não alterado.")
        except ValueError:
            print("Valor inválido, não alterado.")

    nova_quantidade = input("Nova quantidade em estoque: ").strip()
    if nova_quantidade:
        try:
            qtd_int = int(nova_quantidade)
            if qtd_int >= 0 and len(str(qtd_int)) <= 7:
                produto["quantidade_estoque"] = qtd_int
            else:
                print("Quantidade inválida, não alterada.")
        except ValueError:
            print("Valor inválido, não alterado.")

    nova_imagem = input("Nova URL da imagem: ").strip()
    if nova_imagem:
        produto["imagem_url"] = nova_imagem[:500]

    print("\nProduto atualizado com sucesso!")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

atualizar_produto(produtos)

print("\nLista final de produtos:")
for p in produtos:
    print(p)
