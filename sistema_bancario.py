menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("DIgite o valor do depósito: "))
        if valor_deposito >= 0:
            saldo += valor_deposito
            extrato += f"Depósito - R$ {valor_deposito:.2f} \n"
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito precisar ser um número positivo.")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque >=0 and valor_saque <= limite:
            if saldo >= valor_saque:
                if numero_saques < LIMITE_SAQUE:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque - R$ {valor_saque} \n"
                    print("Saque realizado com sucesso.")
                else:
                    print("Você atingiu o limite máximo de saques.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido, digite um valor maior que R$ 0.00 e menor que R$ 500.00.")


    elif opcao == "e":
        if extrato == "":
            print("Não foi realizado nenhuma transação.")
        else:
            extrato += f"\nSaldo: {saldo}"
            print("####### Extrato #######")
            print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")