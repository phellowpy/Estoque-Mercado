categorias = []

def gerar_id(lista, chave="id"):

    if not lista:
        return 1
    else:
        return max(item[chave] for item in lista) + 1

def criar_categoria():

    categoria_id = gerar_id(categorias, "id_categoria")

    marca_id = gerar_id(categorias, "id_marca")

    nome = input("Digite o nome da categoria: ").strip()
    descricao = input("Digite a descrição da categoria: ").strip()
    if len(descricao) > 500:
        descricao = descricao[:500]
        print("Descrição cortada para 500 caracteres.")


    categoria = {
        "id_categoria": categoria_id,
        "id_marca": marca_id,
        "nome": nome,
        "descricao": descricao,
    }

    categorias.append(categoria)

    print("\nCategoria cadastrada com sucesso!")
    print(f"ID Categoria: {categoria_id}, ID Marca: {marca_id}, Nome: {nome}, Descrição: {descricao}")

criar_categoria()

print("\nLista de Categorias:")
for c in categorias:
    print(c)
