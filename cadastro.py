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

def criar_conta(novo_id: int) -> dict:
    print("\n--- Criar Nova Conta ---")

    while True:
        nome = input("Nome: ").strip()
        if len(nome) < 1:
            print("Nome não cumpre o mínimo de caracteres!")
        elif len(nome) > 50:
            print("Nome inválido ou muito longo!")
        else:
            break

    while True:
        email = input("Email: ").strip()
        if not validar_email(email):
            print("Email inválido ou faltando algo!")
        elif len(email) > 100:
            print("Email inválido ou muito longo!")
        else:
            break

    while True:
        telefone = input("Telefone: ").strip()
        if not telefone.isdigit():
            print("Telefone inválido, só aceita números!")
        elif len(telefone) < 11:
            print("Telefone não cumpre o mínimo de caracteres!")
        elif len(telefone) > 11:
            print("Telefone inválido ou muito longo!")
        else:
            break

    while True:
        cpf = input("CPF: ").strip()
        if not cpf.isdigit():
            print("CPF inválido, só aceita números!")
        elif len(cpf) < 11:
            print("CPF não cumpre o mínimo de caracteres!")
        elif len(cpf) > 11:
            print("CPF inválido ou muito longo!")
        else:
            break

    while True:
        contato_extra = input("Contato extra: ").strip()
        if len(contato_extra) > 100:
            print("Contato extra inválido ou muito longo!")
        else:
            break

    while True:
        descricao = input("Descrição: ").strip()
        if len(descricao) > 200:
            print("Descrição inválida ou muito longa!")
        else:
            break

    while True:
        imagem_url = input("URL da imagem: ").strip()
        if len(imagem_url) > 500:
            print("Imagem URL inválida ou muito longa!")
        else:
            break

    while True:
        senha = input("Senha: ").strip()
        if len(senha) < 6:
            print("Senha não cumpre o mínimo de caracteres!")
        elif len(senha) > 50:
            print("Senha inválida ou muito longa!")
        else:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            break

    while True:
        print("\nSelecione o cargo:")
        for i, tipo in enumerate(tipos_conta, start=1):
            print(f"{i} - {tipo}")
        try:
            opcao = int(input("Número da opção: ").strip())
            if 1 <= opcao <= len(tipos_conta):
                cargo = tipos_conta[opcao - 1]
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Digite apenas números correspondentes às opções.")

    return {
        "id": novo_id,
        "nome_conta": nome,
        "email": email,
        "telefone": telefone,
        "cpf": cpf,
        "contato_extra": contato_extra,
        "descricao": descricao,
        "imagem_url": imagem_url,
        "senha": senha,
        "cargo": cargo
    }

nova_conta = criar_conta(1)

print("\n--- Conta Criada ---")
for k, v in nova_conta.items():
    if k == "senha":
        print(f"{k}: {v[:10]}...")
    elif k == "cpf":
        print(f"{k}: {formatar_cpf(v)}")
    elif k == "telefone":
        print(f"{k}: {formatar_tel(v)}")
    else:
        print(f"{k}: {v}")
