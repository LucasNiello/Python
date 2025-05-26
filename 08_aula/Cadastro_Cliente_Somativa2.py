# Sistema de Cadastro de Clientes: armazena dados como nome, telefone, endereço.
# Brenda / João / Lucas / Hayron

clientes = []

def adicionar_cliente():
    """Adiciona um novo cliente à lista."""
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ") # Adicionado campo endereço
    cliente = {"nome": nome, "email": email, "telefone": telefone, "endereco": endereco} # Adicionado endereço ao dicionário
    clientes.append(cliente)
    print("\nCliente adicionado com sucesso!")

def listar_clientes():
    """Lista todos os clientes cadastrados."""
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return
    print("\n--- Lista de Clientes ---")
    for i, cliente in enumerate(clientes):
        print(f"ID: {i}")
        print(f"  Nome: {cliente['nome']}")
        print(f"  Email: {cliente['email']}")
        print(f"  Telefone: {cliente['telefone']}")
        print(f"  Endereço: {cliente['endereco']}") # Exibe o endereço
        print("-" * 20)

def buscar_cliente():
    """Busca um cliente pelo nome."""
    if not clientes:
        print("\nNenhum cliente cadastrado para buscar.")
        return
    termo_busca = input("Digite o nome ou parte do nome para buscar: ").lower()
    encontrados = []
    for i, cliente in enumerate(clientes):
        if termo_busca in cliente['nome'].lower():
            encontrados.append((i, cliente))

    if not encontrados:
        print(f"\nNenhum cliente encontrado com o termo '{termo_busca}'.")
    else:
        print("\n--- Clientes Encontrados ---")
        for i, cliente in encontrados:
            print(f"ID: {i}")
            print(f"  Nome: {cliente['nome']}")
            print(f"  Email: {cliente['email']}")
            print(f"  Telefone: {cliente['telefone']}")
            print(f"  Endereço: {cliente['endereco']}") # Exibe o endereço
            print("-" * 20)

def remover_cliente():
    """Remove um cliente pelo ID."""
    listar_clientes()
    if not clientes:
        return

    try:
        id_remover = int(input("\nDigite o ID do cliente que deseja remover: "))
        if 0 <= id_remover < len(clientes):
            cliente_removido = clientes.pop(id_remover)
            print(f"\nCliente '{cliente_removido['nome']}' removido com sucesso!")
        else:
            print("\nID inválido.")
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número correspondente ao ID.")
    except IndexError:
         print("\nID fora do intervalo válido.")

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n--- Sistema de Cadastro de Clientes ---")
    print("1. Adicionar Cliente")
    print("2. Listar Clientes")
    print("3. Buscar Cliente")
    print("4. Remover Cliente")
    print("5. Sair")
    print("-" * 37)

def main():
    """Função principal que executa o loop do programa."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            buscar_cliente()
        elif opcao == '4':
            remover_cliente()
        elif opcao == '5':
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

# O código implementa um sistema de cadastro de clientes com funcionalidades para adicionar, listar, buscar e remover clientes.
# Cada cliente é representado por um dicionário contendo nome, email, telefone e endereço.
