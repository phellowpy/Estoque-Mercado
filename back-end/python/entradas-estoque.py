import datetime

class EntradaEstoque:
    def __init__(self, id_entrada, id_localizacao, id_fornecedor, id_produto, quantidade, data_entrada, origem, observacao):
        self.id_entrada = id_entrada
        self.id_localizacao = id_localizacao
        self.id_fornecedor = id_fornecedor
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.data_entrada = data_entrada
        self.origem = origem
        self.observacao = observacao

    def __str__(self):
        return (f"--- Entrada de Estoque ---\n"
                f"ID Entrada: {self.id_entrada}\n"
                f"ID Localização: {self.id_localizacao}\n"
                f"ID Fornecedor: {self.id_fornecedor}\n"
                f"ID Produto: {self.id_produto}\n"
                f"Quantidade: {self.quantidade}\n"
                f"Data de Entrada: {self.data_entrada}\n"
                f"Origem: {self.origem}\n"
                f"Observação: {self.observacao}\n")

def get_int_input(pergunta):
    while True:
        try:
            valor = int(input(pergunta))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

def cadastrar_entrada_estoque():
    
    id_localizacao = get_int_input("Digite o ID da localização: ")
    id_fornecedor = get_int_input("Digite o ID do fornecedor: ")
    id_produto = get_int_input("Digite o ID do produto: ")
    quantidade = get_int_input("Digite a quantidade: ")
    
    origem = input("Digite a origem da mercadoria: ")
    observacao = input("Digite a observação: ")

    id_entrada = 1 
    data_entrada = datetime.datetime.now()

    nova_entrada = EntradaEstoque(
        id_entrada=id_entrada,
        id_localizacao=id_localizacao,
        id_fornecedor=id_fornecedor,
        id_produto=id_produto,
        quantidade=quantidade,
        data_entrada=data_entrada,
        origem=origem,
        observacao=observacao
    )
    
    print("\nEntrada de estoque registrada com sucesso!")
    print(nova_entrada)

if __name__ == "__main__":
    cadastrar_entrada_estoque()