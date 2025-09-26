class Fornecedor:
    def __init__(self, id_fornecedor, nome_fornecedor, cnpj, telefone, contato, endereco):
        self.id_fornecedor = id_fornecedor
        self.nome_fornecedor = nome_fornecedor
        self.cnpj = cnpj
        self.ddd = telefone[:2]
        self.telefone_numero = telefone[2:]
        self.contato = contato
        self.endereco = endereco

    def __str__(self):
        return (f"--- Fornecedor ---\n"
                f"ID: {self.id_fornecedor}\n"
                f"Nome: {self.nome_fornecedor}\n"
                f"CNPJ: {self.cnpj}\n"
                f"Telefone: ({self.ddd}) {self.telefone_numero}\n"
                f"Contato: {self.contato}\n"
                f"Endereço: {self.endereco}\n")

class LocalEstoque:
    def __init__(self, id_localizacao, id_produto, setor, prateleira, observacao):
        self.id_localizacao = id_localizacao
        self.id_produto = id_produto
        self.setor = setor
        self.prateleira = prateleira
        self.observacao = observacao

    def __str__(self):
        return (f"--- Local de Estoque ---\n"
                f"ID Localização: {self.id_localizacao}\n"
                f"ID Produto: {self.id_produto}\n"
                f"Setor: {self.setor}\n"
                f"Prateleira: {self.prateleira}\n"
                f"Observação: {self.observacao}\n")

PRODUTOS_CADASTRADOS = [
    {"id_produto": 1, "nome": "Arroz", "localizacao": None},
    {"id_produto": 2, "nome": "Feijão", "localizacao": None},
    {"id_produto": 3, "nome": "Macarrão", "localizacao": None},
]

USUARIO_PADRAO = "joao@example.com"
SENHA_PADRAO = "12345"

def login():
    print("--- Login ---")
    email = input("E-mail: ")
    senha = input("Senha: ")
    if email == USUARIO_PADRAO and senha == SENHA_PADRAO:
        print("\nLogin bem-sucedido!")
        return True
    else:
        print("E-mail ou senha incorretos.")
        return False

def validar_numero(campo, comprimento_minimo, comprimento_maximo):
    while True:
        entrada = input(f"Digite o {campo}: ")
        
        if not entrada.isdigit():
            print(f"{campo} inválido!")
        elif len(entrada) < comprimento_minimo:
            print(f"{campo} muito pequeno!")
        elif len(entrada) > comprimento_maximo:
            print(f"{campo} muito longo!")
        else:
            return entrada

def listar_produtos():
    print("\n--- Produtos Disponíveis ---")
    for produto in PRODUTOS_CADASTRADOS:
        print(f"ID: {produto['id_produto']} - Nome: {produto['nome']}")

def atualizar_local_estoque():
    print("\n--- Atualizar Localização de Estoque ---")
    listar_produtos()
    
    try:
        id_produto_escolhido = int(input("Digite o ID do produto que deseja atualizar: "))
        
        produto_encontrado = None
        for p in PRODUTOS_CADASTRADOS:
            if p["id_produto"] == id_produto_escolhido:
                produto_encontrado = p
                break
        
        if not produto_encontrado:
            print("ID de produto não encontrado.")
            return

        print(f"\nAtualizando localização para: {produto_encontrado['nome']}")
        
        setor = input("Digite o novo setor: ")
        prateleira = input("Digite a nova prateleira: ")
        observacao = input("Digite a nova observação: ")

        novo_local = LocalEstoque(
            id_localizacao=len(PRODUTOS_CADASTRADOS) + 1,
            id_produto=id_produto_escolhido,
            setor=setor,
            prateleira=prateleira,
            observacao=observacao
        )
        
        produto_encontrado["localizacao"] = novo_local
        
        print("\nLocal de estoque atualizado com sucesso!")
        print(novo_local)
    except ValueError:
        print("Entrada inválida. Digite um ID numérico.")

if __name__ == "__main__":
    if login():
        atualizar_local_estoque()
    else:
        print("Acesso negado. O programa será encerrado.")