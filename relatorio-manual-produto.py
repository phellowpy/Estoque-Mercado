from datetime import datetime

produtos = [
    {"id_produto": 1, "nome_produto": "Arroz", "quantidade": 50},
    {"id_produto": 2, "nome_produto": "Feijão", "quantidade": 30},
    {"id_produto": 3, "nome_produto": "Macarrão", "quantidade": 40}
]

usuarios = [
    {"id_usuario": 1, "email": "joao@email.com", "senha": "1234"}
]

ajustes = []

def gerar_id(lista, chave):
    if not lista:
        return 1
    return max(item[chave] for item in lista) + 1

def login():
    print("\n--- Login ---")
    while True:
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        usuario = next((u for u in usuarios if u["email"] == email and u["senha"] == senha), None)
        if usuario:
            print("\nLogin realizado com sucesso!\n")
            return usuario
        print("Credenciais inválidas. Tente novamente.")

def cadastrar_ajuste(usuario):
    print("\n--- Produtos Disponíveis ---")
    for p in produtos:
        print(f"{p['id_produto']} - {p['nome_produto']} (Qtd: {p['quantidade']})")
    try:
        id_produto = int(input("Digite o ID do produto: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    produto = next((p for p in produtos if p["id_produto"] == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    try:
        quantidade = int(input("Digite a quantidade ajustada: ").strip())
    except ValueError:
        print("Quantidade inválida.")
        return
    motivo = input("Digite o motivo do ajuste: ").strip()
    if not motivo or len(motivo) > 255:
        print("Motivo inválido ou muito longo.")
        return
    ajuste = {
        "id_ajuste": gerar_id(ajustes, "id_ajuste"),
        "id_produto": id_produto,
        "id_usuario": usuario["id_usuario"],
        "quantidade_ajustada": quantidade,
        "motivo": motivo,
        "data_ajuste": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ajustes.append(ajuste)
    print("\nAjuste cadastrado com sucesso!")
    print(ajuste)

usuario_logado = login()
cadastrar_ajuste(usuario_logado)
