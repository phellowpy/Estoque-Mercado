class HistoricoMovimentacoes:
    def __init__(self, id_movimentacao, id_produto, tipo, quantidade):
        self.id_movimentacao = id_movimentacao
        self.id_produto = id_produto
        self.tipo = tipo
        self.quantidade = quantidade

    def __str__(self):
        return (f"--- Histórico de Movimentação ---\n"
                f"ID Movimentação: {self.id_movimentacao}\n"
                f"ID Produto: {self.id_produto}\n"
                f"Tipo: {self.tipo}\n"
                f"Quantidade: {self.quantidade}\n")

def get_int_input(pergunta):
    while True:
        try:
            valor = int(input(pergunta))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

def registrar_historico():
    
    id_produto = get_int_input("Digite o ID do produto: ")
    
    while True:
        tipo = input("Digite o tipo da movimentação (ENTRADA ou SAIDA): ").upper()
        if tipo in ["ENTRADA", "SAIDA"]:
            break
        else:
            print("Tipo inválido. Por favor, digite ENTRADA ou SAIDA.")
            
    quantidade = get_int_input("Digite a quantidade: ")
    
    id_movimentacao = 1 

    novo_registro = HistoricoMovimentacoes(
        id_movimentacao=id_movimentacao,
        id_produto=id_produto,
        tipo=tipo,
        quantidade=quantidade
    )
    
    print("\nRegistro de movimentação criado com sucesso!")
    print(novo_registro)

if __name__ == "__main__":
    registrar_historico()