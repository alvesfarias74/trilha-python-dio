def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    cpf = "".join(filter(str.isdigit, cpf))

    usuario_existente = any(usuario["cpf"] == cpf for usuario in usuarios)

    if usuario_existente:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def encontrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": agencia,
            "numero": numero_conta,
            "usuario": usuario
        })
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado. Criação de conta falhou.")


def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero']}")
        print(f"Titular: {conta['usuario']['nome']}")


# Programa principal
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        criar_conta(AGENCIA, contas, usuarios)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")