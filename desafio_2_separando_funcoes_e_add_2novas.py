# Função para cadastrar um novo usuário (cliente)
def cadastrar_usuario(clientes, nome, data_nascimento, cpf, endereco):
    # Verificar se o CPF já existe na lista de clientes
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return

    # Adicionar o novo usuário à lista de clientes
    clientes.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })

# Função para cadastrar uma nova conta bancária vinculada a um cliente
def cadastrar_conta(contas, agencia, cliente):
    # Gerar o número da conta sequencialmente
    numero_conta = len(contas) + 1

    # Adicionar a nova conta à lista de contas
    contas.append({
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cliente': cliente
    })

# Função de saque (recebe argumentos apenas por nome - keyword only)
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato

# Função de depósito (recebe argumentos apenas por posição - positional only)
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Função de exibir extrato (recebe argumentos por posição e nome)
def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Lista para armazenar os clientes
clientes = []

# Lista para armazenar as contas bancárias
contas = []

# Agência fixa
agencia_fixa = "0001"

# Menu de opções
menu = """
[c] Cadastrar usuário
[cc] Cadastrar conta bancária
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "c":
        nome = input("Nome do cliente: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF (apenas números): ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")
        cadastrar_usuario(clientes, nome, data_nascimento, cpf, endereco)

    elif opcao == "cc":
        cpf_cliente = input("CPF do cliente vinculado à conta: ")
        cliente_encontrado = False

        for cliente in clientes:
            if cliente['cpf'] == cpf_cliente:
                cadastrar_conta(contas, agencia_fixa, cliente)
                cliente_encontrado = True
                break

        if not cliente_encontrado:
            print("Erro: Cliente não encontrado.")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
