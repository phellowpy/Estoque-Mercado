import itertools
import hashlib

id_generator = itertools.count(1)

tipos_conta = [
    "admin",
    "gerente",
    "supervisor",
    "estoquista",
    "caixa",
    "auditor",
    "tecnico_ti"
]

contas = []

while True:
    print("\n--- Cadastro de Conta ---")
    conta_id = next(id_generator)

    while True:
        nome_conta = input("Digite o nome da conta: ").strip()
        if 1 <= len(nome_conta) <= 50:
            break
        else:
            print("Nome inválido ou muito longo!")

    while True:
        email = input("Digite o email da conta: ").strip()
        if (
            1 <= len(email) <= 100
            and "@" in email
            and len(email.split("@")[0]) >= 3
        ):
            break
        else:
            print("Email inválido ou muito longo!")

    while True:
        telefone = input("Digite o telefone: ").strip()
        if telefone.isdigit() and len(telefone) == 11:
            break
        else:
            print("Telefone inválido ou muito longo!")

    while True:
        senha = input("Digite a senha da conta: ").strip()
        if 6 <= len(senha) <= 50:
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            break
        else:
            print("Senha inválida ou muito longa/curta!")

    print("\nSelecione o cargo da conta:")
    for i, tipo in enumerate(tipos_conta, start=1):
        print(f"{i} - {tipo}")

    while True:
        try:
            opcao = int(input("Digite o número da opção: "))
            if 1 <= opcao <= len(tipos_conta):
                tipo_conta = tipos_conta[opcao - 1]
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Digite um número válido.")

    conta = {
        "id": conta_id,
        "nome_conta": nome_conta,
        "email": email,
        "telefone": telefone,
        "senha": senha_hash,
        "cargo": tipo_conta
    }

    contas.append(conta)

    print("\nConta cadastrada com sucesso!\n")
    print(conta)

    continuar = input("\nDeseja cadastrar outra conta? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\nTodas as contas cadastradas:")
for c in contas:
    print(c)
