import datetime

class SaidaEstoque:
    def __init__(self, id_saida, id_produto, quantidade, data_saida, destino, observacao):
        self.id_saida = id_saida
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.data_saida = data_saida
        self.destino = destino
        self.observacao = observacao

    def __str__(self):
        return (f"--- Saída de Estoque ---\n"
                f"ID Saída: {self.id_saida}\n"
                f"ID Produto: {self.id_produto}\n"
                f"Quantidade: {self.quantidade}\n"
                f"Data de Saída: {self.data_saida}\n"
                f"Destino: {self.destino}\n"
                f"Observação: {self.observacao}\n")

def get_int_input(pergunta):
    while True:
        try:
            valor = int(input(pergunta))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

def registrar_saida_estoque():
    
    id_produto = get_int_input("Digite o ID do produto: ")
    quantidade = get_int_input("Digite a quantidade que saiu do estoque: ")
    
    destino = input("Digite o destino da mercadoria: ")
    observacao = input("Digite a observação (opcional: ")

    id_saida = 1
    data_saida = datetime.datetime.now()

    nova_saida = SaidaEstoque(
        id_saida=id_saida,
        id_produto=id_produto,
        quantidade=quantidade,
        data_saida=data_saida,
        destino=destino,
        observacao=observacao
    )
    
    print("\nSaída de estoque registrada com sucesso!")
    print(nova_saida)

if __name__ == "__main__":
    registrar_saida_estoque()