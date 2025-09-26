marcas = []
fornecedores = []

def gerar_id(lista, chave="id"):
    if not lista:
        return 1
    else:
        return max(item[chave] for item in lista) + 1

def criar_fornecedor(nome_fornecedor):
    id_fornecedor = gerar_id(fornecedores, "id_fornecedor")
    fornecedor = {"id_fornecedor": id_fornecedor, "nome_fornecedor": nome_fornecedor}
    fornecedores.append(fornecedor)
    return fornecedor

def criar_marca():
    id_marca = gerar_id(marcas, "id_marca")

    nome_marca = input("Digite o nome da marca: ").strip()
    if not nome_marca or len(nome_marca) > 100:
        print("Nome da marca inválido (máx 100 caracteres).")
        return

    pais_origem = input("Digite o país de origem: ").strip()
    if not pais_origem or len(pais_origem) > 80:
        print("País de origem inválido (máx 80 caracteres).")
        return

    prioridade_prateleira = input("Digite a prioridade na prateleira (ex: A1, B2): ").strip()
    if not prioridade_prateleira or len(prioridade_prateleira) > 5:
        print("Prioridade inválida (máx 5 caracteres).")
        return

    fornecedor = fornecedores[0]  

    marca = {
        "id_marca": id_marca,
        "id_fornecedor": fornecedor["id_fornecedor"],
        "nome_marca": nome_marca,
        "pais_origem": pais_origem,
        "prioridade_prateleira": prioridade_prateleira
    }

    marcas.append(marca)

    print("\nMarca cadastrada com sucesso!")
    for k, v in marca.items():
        print(f"{k}: {v}")

criar_fornecedor("Fornecedor X")
criar_marca()

print("\nLista de Marcas:")
for m in marcas:
    print(m)

