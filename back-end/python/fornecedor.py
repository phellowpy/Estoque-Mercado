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
        return f"ID: {self.id_fornecedor}\n" \
               f"Nome: {self.nome_fornecedor}\n" \
               f"CNPJ: {self.cnpj}\n" \
               f"Telefone: ({self.ddd}) {self.telefone_numero}\n" \
               f"Contato: {self.contato}\n" \
               f"Endereço: {self.endereco}\n"

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

def cadastrar_fornecedor():
    
    nome = input("Digite o nome do fornecedor: ")
    contato = input("Digite o nome do contato: ")
    endereco = input("Digite o endereço: ")

    cnpj = validar_numero("CNPJ", 14, 14)
    telefone = validar_numero("telefone", 10, 11)

    novo_fornecedor = Fornecedor(1, nome, cnpj, telefone, contato, endereco)
    
    print("\nFornecedor cadastrado com sucesso!")
    print(novo_fornecedor)

if __name__ == "__main__":
    cadastrar_fornecedor()