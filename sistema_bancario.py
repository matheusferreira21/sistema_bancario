#No criar usuário, falta verificar se o cpf é so numero


#Função de deposito
def deposito(saldo, valor, extrato):
    if valor >= 0:
        saldo += valor
        extrato += f"Depósito - R$ {valor:.2f} \n"
        print("Depósito realizado com sucesso.")
    else:
        print("O valor do depósito precisar ser um número positivo.")
    return saldo,extrato

# Função de saque com verficação
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

# Mostrar o extrato
def mostrar_extrato(extrato,saldo):
    if extrato == "":
        print("Não foi realizado nenhuma transação.")
    else:
        print("####### Extrato #######")
        print(extrato)
        print(f"\nSaldo: {saldo}")

# Criar novo cliente
def criar_usuario():
    usuario = []
    endereco = ""
    cpf = ""

    usuario.append(input("digite o nome do cliente: "))
    usuario.append(input("digite a data de nascimento: "))

    while True:
        cpf = input("digite o CPF: ")

        if verificar_cpf(cpf) == 1 or cpf.isnumeric() == False:
            print("O CPF digitado é inválido")
        else:
            usuario.append(cpf)
            break

    endereco += input("digite o logradouro: ")+", "
    endereco += input("digite o número do endereço: ") + " - "
    endereco += input("digite o bairro: ") + " - "
    endereco += input("digite a cidade: ") + "/"
    endereco += input("digite a sigla do estado: ")

    usuario.append(endereco)
    print("O cliente foi cadastrado com sucesso!")
    return usuario

#listar usuarios
def lista_usuarios():
    contador = 0
    for usuario in usuarios:
        print(str(contador) + f": Nome do cliente {usuario[0]}, data de nascimento: {usuario[1]}, CPF: {usuario[2]}, Endereço: {usuario[3]} ")
        contador += 1

# Verificar se o cpf já existe
def verificar_cpf(cpf):
    for usuario in usuarios:
        tem_quantos_cpf_iguais = usuario[2].count(cpf)
        if tem_quantos_cpf_iguais == 1:
            return 1
    return 0

#criar conta corrente
def criar_conta_corrente(numero_conta):
    NUMERO_AGENCIA = "0001"
    conta = []
    cpf = ""

    conta.append("Agência: "+ NUMERO_AGENCIA)
    conta.append("Numero da conta: "+ str(numero_conta))

    while True:
        cpf = input("Digite o CPF do cliente: ")

        if verificar_cpf(cpf) == 1:
            conta.append(cpf)
            break
        else:
            print("O CPF digitado não existe.")
    
    print("Conta corrente criada com sucesso")
    return conta


def listar_conta_correntes():
    for conta in contas:
        for usuario in usuarios:
            if usuario[2] == conta[2]:
                print(conta[0] + ", " + conta[1]+", Nome do titular: "+ usuario[0])

menu = """
#### Cliente ####

[u] criar cliente
[c] criar conta corrente
[l] listar cliente
[r] listar contas correntes

##### Acões #####

[d] depositar
[s] sacar
[e] extrato

#################
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
usuarios = []
contas = []
numero_conta = 1

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
        
    elif opcao == "u":
        usuarios.append(criar_usuario())

    elif opcao == "c":
        contas.append(criar_conta_corrente(numero_conta))
        numero_conta += 1

    elif opcao == "l":
        lista_usuarios()

    elif opcao == "r":
        listar_conta_correntes()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


