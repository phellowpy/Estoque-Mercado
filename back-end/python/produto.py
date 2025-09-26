def gerar_id(lista, chave="id"):
    if not lista:
        return 1
    else:
        return max(item[chave] for item in lista) + 1

produtos = []
fornecedores = []
categorias = []
marcas = []
localizacoes = []

def cadastrar_fornecedor():
    fornecedor_id = gerar_id(fornecedores, "id_fornecedor")
    nome = input("Digite o nome do fornecedor: ").strip()
    fornecedor = {"id_fornecedor": fornecedor_id, "nome": nome}
    fornecedores.append(fornecedor)
    return fornecedor_id

def cadastrar_categoria():
    categoria_id = gerar_id(categorias, "id_categoria")
    nome = input("Digite o nome da categoria: ").strip()
    categoria = {"id_categoria": categoria_id, "nome": nome}
    categorias.append(categoria)
    return categoria_id

def cadastrar_marca():
    marca_id = gerar_id(marcas, "id_marca")
    nome = input("Digite o nome da marca: ").strip()
    marca = {"id_marca": marca_id, "nome": nome}
    marcas.append(marca)
    return marca_id

def cadastrar_localizacao():
    local_id = gerar_id(localizacoes, "id_localizacao")
    nome = input("Digite o nome da localização: ").strip()
    local = {"id_localizacao": local_id, "nome": nome}
    localizacoes.append(local)
    return local_id

def cadastrar_produto():
    produto_id = gerar_id(produtos, "id_produto")

    id_fornecedor = cadastrar_fornecedor()
    id_categoria = cadastrar_categoria()
    id_marca = cadastrar_marca()
    id_localizacao = cadastrar_localizacao()

    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        if 1 <= len(nome_produto) <= 150:
            break
        print("Nome inválido! (máx 150 caracteres)")

    descricao = input("Digite a descrição do produto: ").strip()
    if len(descricao) > 500:
        descricao = descricao[:500]
        print("Descrição cortada para 500 caracteres.")

    while True:
        try:
            preco = float(input("Digite o preço do produto: ").replace(",", "."))
            if preco >= 0:
                break
            else:
                print("Preço não pode ser negativo.")
        except ValueError:
            print("Digite um valor válido.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade >= 0 and len(str(quantidade)) <= 7:
                break
            else:
                print("Quantidade inválida (máx 7 dígitos).")
        except ValueError:
            print("Digite um número válido.")

    imagem_url = input("Digite o link da imagem do produto: ").strip()
    if len(imagem_url) > 500:
        imagem_url = imagem_url[:500]
        print("URL cortada para 500 caracteres.")

    produto = {
        "id_produto": produto_id,
        "id_fornecedor": id_fornecedor,
        "id_localizacao": id_localizacao,
        "id_categoria": id_categoria,
        "id_marca": id_marca,
        "nome_produto": nome_produto,
        "descricao": descricao,
        "preco": preco,
        "quantidade_estoque": quantidade,
        "imagem_url": imagem_url
    }

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!\n")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

while True:
    cadastrar_produto()
    continuar = input("\nDeseja cadastrar outro produto? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\nProdutos cadastrados:")
for p in produtos:
    print(p)
