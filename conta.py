import hashlib

# conta de exemplo pra puxar dado
conta = {
    "id": 1,
    "nome_conta": "Joao",
    "email": "joao@email.com",
    "telefone": "11987654321",
    "senha": hashlib.sha256("123456".encode()).hexdigest(),
    "cargo": "caixa"
}

tipos_conta = [
    "admin",
    "gerente",
    "supervisor",
    "estoquista",
    "caixa",
    "auditor",
    "tecnico_ti"
]

print("\nConta atual:")
for k, v in conta.items():
    if k == "senha":
        print(f"{k}: {v[:10]}... ")
    else:
        print(f"{k}: {v}")

print("\n--- Editar Conta ---")

novo_nome = input("Novo nome (ou Enter para manter): ").strip()
if novo_nome and 1 <= len(novo_nome) <= 50:
    conta["nome_conta"] = novo_nome

novo_email = input("Novo email (ou Enter para manter): ").strip()
if novo_email and 1 <= len(novo_email) <= 100:
    conta["email"] = novo_email

while True:
    novo_tel = input("Novo telefone (11 dígitos, ou Enter para manter): ").strip()
    if not novo_tel:
        break
    if novo_tel.isdigit() and len(novo_tel) == 11:
        conta["telefone"] = novo_tel
        break
    else:
        print("Telefone inválido!")

nova_senha = input("Nova senha (6-50 caracteres, ou Enter para manter): ").strip()
if nova_senha:
    if 6 <= len(nova_senha) <= 50:
        conta["senha"] = hashlib.sha256(nova_senha.encode()).hexdigest()
    else:
        print("Senha inválida! Mantida a anterior.")

print("\nSelecione o cargo (ou Enter para manter):")
for i, tipo in enumerate(tipos_conta, start=1):
    print(f"{i} - {tipo}")

opcao = input("Digite o número da opção: ").strip()
if opcao.isdigit():
    opcao = int(opcao)
    if 1 <= opcao <= len(tipos_conta):
        conta["cargo"] = tipos_conta[opcao - 1]

print("\nConta editada com sucesso!\n")
for k, v in conta.items():
    if k == "senha":
        print(f"{k}: {v[:10]}... (hash)")
    else:
        print(f"{k}: {v}")
