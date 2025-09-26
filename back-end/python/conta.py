import hashlib

tipos_conta = [
    "admin",
    "gerente",
    "supervisor",
    "estoquista",
    "caixa",
    "auditor",
    "tecnico_ti"
]

conta = {
    "id": 1,
    "nome_conta": "Joao",
    "email": "joao@email.com",
    "telefone": "11987654321",
    "cpf": "12345678901",
    "contato_extra": "11912345678",
    "descricao": "Funcionário exemplo do setor de caixa.",
    "imagem_url": "http://exemplo.com/foto.jpg",
    "senha": hashlib.sha256("123456".encode()).hexdigest(),
    "cargo": "caixa"
}

def formatar_cpf(cpf: str) -> str:
    if len(cpf) == 11:
        return cpf[:3] + "*" * 6 + cpf[-2:]
    return cpf

def formatar_tel(telefone: str) -> str:
    if len(telefone) == 11 and telefone.isdigit():
        return f"({telefone[:2]}) {telefone[2:]}"
    return telefone

def validar_email(email: str) -> bool:
    if "@" not in email:
        return False
    parte_local = email.split("@")[0]
    return len(parte_local) >= 3

def login(conta: dict) -> bool:
    print("\n--- Login ---")
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    if email == conta["email"] and senha_hash == conta["senha"]:
        print("Login bem-sucedido!")
        return True
    print("Email ou senha incorretos!")
    return False

def editar_conta(conta: dict) -> dict:
    print("\n--- Editar Conta ---")
    
    def input_edit(prompt, atual, max_len=None, only_digits=False, min_len=None):
        while True:
            valor = input(f"{prompt} [{atual}]: ").strip()
            if valor == "":
                return atual
            if only_digits and not valor.isdigit():
                print("Somente números são aceitos!")
                continue
            if min_len and len(valor) < min_len:
                print(f"Não cumpre o mínimo de {min_len} caracteres!")
                continue
            if max_len and len(valor) > max_len:
                print("Muito longo!")
                continue
            return valor

    conta["nome_conta"] = input_edit("Nome", conta["nome_conta"], max_len=50, min_len=1)
    
    while True:
        email = input_edit("Email", conta["email"], max_len=100)
        if validar_email(email):
            conta["email"] = email
            break
        print("Email inválido!")

    conta["telefone"] = input_edit("Telefone", conta["telefone"], max_len=11, min_len=11, only_digits=True)
    conta["cpf"] = input_edit("CPF", conta["cpf"], max_len=11, min_len=11, only_digits=True)
    conta["contato_extra"] = input_edit("Contato extra", conta["contato_extra"], max_len=100)
    conta["descricao"] = input_edit("Descrição", conta["descricao"], max_len=200)
    conta["imagem_url"] = input_edit("URL da imagem", conta["imagem_url"], max_len=500)

    senha_nova = input("Nova senha (deixe em branco para manter atual): ").strip()
    if senha_nova:
        if 6 <= len(senha_nova) <= 50:
            conta["senha"] = hashlib.sha256(senha_nova.encode()).hexdigest()
        else:
            print("Senha inválida, mantendo a atual!")

    print("\nSelecione o cargo:")
    for i, tipo in enumerate(tipos_conta, start=1):
        print(f"{i} - {tipo}")
    try:
        opcao = int(input(f"Número da opção [{tipos_conta.index(conta['cargo']) + 1}]: ").strip() or (tipos_conta.index(conta['cargo']) + 1))
    except ValueError:
        opcao = tipos_conta.index(conta['cargo']) + 1
    if 1 <= opcao <= len(tipos_conta):
        conta["cargo"] = tipos_conta[opcao - 1]

    return conta

if login(conta):
    conta = editar_conta(conta)
    print("\n--- Conta Atualizada ---")
    for k, v in conta.items():
        if k == "senha":
            print(f"{k}: {v[:10]}")
        elif k == "cpf":
            print(f"{k}: {formatar_cpf(v)}")
        elif k == "telefone":
            print(f"{k}: {formatar_tel(v)}")
        else:
            print(f"{k}: {v}")
