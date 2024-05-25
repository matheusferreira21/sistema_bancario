

def deposito(saldo, valor, extrato):
    if valor >= 0:
        saldo += valor
        extrato += f"Depósito - R$ {valor:.2f} \n"
        print("Depósito realizado com sucesso.")
    else:
        print("O valor do depósito precisar ser um número positivo.")
    return saldo,extrato


def saque(valor_saque, limite, saldo, numero_saques, LIMITE_SAQUE, extrato):
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

    return saldo, extrato, numero_saques

def mostrar_extrato(extrato,saldo):
    if extrato == "":
        print("Não foi realizado nenhuma transação.")
    else:
        print("####### Extrato #######")
        print(extrato)
        print(f"\nSaldo: {saldo}")

def criar_usuario():
    print("criar usuario")

def criar_conta_corrent():
    print("criar conta_corrente")

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
lista_usuarios = {}

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor_deposito,extrato)
      

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        saldo, extrato, numero_saques =saque(valor_saque=valor_saque, limite=limite, saldo=saldo, numero_saques=numero_saques, LIMITE_SAQUE=LIMITE_SAQUE, extrato=extrato)


    elif opcao == "e":
        mostrar_extrato(extrato,saldo=saldo)
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


