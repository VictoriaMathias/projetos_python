menu = """

------------- BANCO VALENCIA --------------

Selecione a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

def depositar(saldo, extrato):
            
    valor_deposito = float(input("""    ==> Depósito    
              
    Digite o valor que você deseja depositar:

    """))
            
    saldo += valor_deposito
    extrato += f"\nDepósito = R$ {valor_deposito:.2f}\n"
    print(f"\n Depósito de R$ {valor_deposito:.2f} realizado com sucesso!\n")

    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite_saques):

    if numero_saques >= limite_saques:
        print("\n Limite de saques atingido! Você não pode sacar mais.\n")
        return saldo, extrato, numero_saques

    valor_saque = float(input("""    ==> Saque    
                
    Digite o valor que você deseja sacar:
                              
    Valor limite por saque: R$ 500,00

    """))

    if valor_saque < saldo:
        print("Saldo insuficiente! Não foi possível realizar o saque.")

    if valor_saque > 0 and valor_saque <= limite:
        saldo -= valor_saque
        extrato += f"\nSaque = R$ {valor_saque:.2f}\n"
        print(f"\n Saque de R$ {valor_saque:.2f} realizado com sucesso!\n")

    else:
        print("Não é possível realizar saques acima de R$ 500,00. Selecione um novo valor!")

    return saldo, extrato, numero_saques



while True:

    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite_saques)

    elif opcao == "3":
        print(f"""

============= Extrato ================
                    
{extrato}

Saldo = R$ {saldo:.2f}

""")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção Inválida. ")