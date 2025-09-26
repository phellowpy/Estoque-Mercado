from datetime import datetime

produtos = [
    {"id_produto": 1, "nome_produto": "Arroz", "preco": 20.0},
    {"id_produto": 2, "nome_produto": "Feijão", "preco": 10.0},
    {"id_produto": 3, "nome_produto": "Macarrão", "preco": 8.0},
]

promocoes = []

def gerar_id(lista, chave="id_promocao"):
    if not lista:
        return 1
    return max(item[chave] for item in lista) + 1

def cadastrar_promocao():
    print("\n--- Produtos Disponíveis ---")
    for produto in produtos:
        print(f"{produto['id_produto']}: {produto['nome_produto']} (Preço: {produto['preco']})")

    while True:
        try:
            id_produto = int(input("Digite o ID do produto para a promoção: "))
            produto_selecionado = next((p for p in produtos if p["id_produto"] == id_produto), None)
            if produto_selecionado:
                break
            print("Produto não encontrado.")
        except ValueError:
            print("Digite um ID válido.")

    while True:
        titulo = input("Título da promoção: ").strip()
        if 1 <= len(titulo) <= 150:
            break
        print("Título inválido (máx 150 caracteres).")

    descricao = input("Descrição da promoção: ").strip()
    if len(descricao) > 150:
        descricao = descricao[:150]
        print("Descrição cortada para 150 caracteres.")

    while True:
        try:
            preco_promocional = float(input(f"Preço promocional (produto atual {produto_selecionado['preco']}): ").replace(",", "."))
            if 0 <= preco_promocional < produto_selecionado["preco"]:
                break
            print("Preço promocional deve ser menor que o preço normal e não negativo.")
        except ValueError:
            print("Digite um valor válido.")

    while True:
        data_inicio = input("Data de início (YYYY-MM-DD HH:MM): ").strip()
        data_fim = input("Data de fim (YYYY-MM-DD HH:MM): ").strip()
        try:
            dt_inicio = datetime.strptime(data_inicio, "%Y-%m-%d %H:%M")
            dt_fim = datetime.strptime(data_fim, "%Y-%m-%d %H:%M")
            if dt_inicio < dt_fim:
                break
            print("Data de início deve ser antes da data de fim.")
        except ValueError:
            print("Formato de data inválido. Use YYYY-MM-DD HH:MM")

    promocao_id = gerar_id(promocoes)
    promocao = {
        "id_promocao": promocao_id,
        "id_produto": id_produto,
        "titulo_promocao": titulo,
        "descricao": descricao,
        "preco_promocional": preco_promocional,
        "data_inicio": dt_inicio.strftime("%Y-%m-%d %H:%M:%S"),
        "data_fim": dt_fim.strftime("%Y-%m-%d %H:%M:%S")
    }

    promocoes.append(promocao)
    print("\nPromoção cadastrada com sucesso!")
    for k, v in promocao.items():
        print(f"{k}: {v}")

while True:
    cadastrar_promocao()
    continuar = input("\nDeseja cadastrar outra promoção? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\nPromoções cadastradas:")
for p in promocoes:
    print(p)