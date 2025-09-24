import hashlib

conta_teste = {
    "id": 1,
    "nome_conta": "ContaTeste",
    "email": "teste@exemplo.com",
    "telefone": "11999998888",
    "senha": hashlib.sha256("senha123".encode()).hexdigest(),
    "cargo": "admin"
}

contas = [conta_teste]

def encontrar_conta_por_email(email):
    for c in contas:
        if c["email"].lower() == email.lower():
            return c
    return None

def tentar_login(max_tentativas=5):
    tentativas = 0
    while tentativas < max_tentativas:
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()

        conta = encontrar_conta_por_email(email)
        if not conta:
            print("Conta não encontrada.")
            tentativas += 1
            continue

        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        if senha_hash == conta["senha"]:
            print("\nLogin realizado com sucesso!\n")
            mostrar_conta_conectada(conta)
            return True
        else:
            print("Senha incorreta.")
            tentativas += 1

    print("\nMuitas tentativas falhas. Acesso bloqueado.")
    return False

def mostrar_conta_conectada(conta):
    print("=== Dados da Conta Conectada ===")
    print(f"ID: {conta['id']}")
    print(f"Nome: {conta['nome_conta']}")
    print(f"Email: {conta['email']}")
    print(f"Telefone: {conta['telefone']}")
    print(f"Cargo: {conta['cargo']}")
    print(f"Senha (hash): {conta['senha'][:12]}...")

if __name__ == "__main__":
    print("Login - use a conta de teste:")
    print("email: teste@exemplo.com")
    print("senha: senha123\n")
    tentar_login()
