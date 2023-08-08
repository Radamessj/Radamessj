Menu = """

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=> """

Saldo = 0
Limite = 1000
Extrato = ""
Numero_de_Saque = 0
Limite_de_Saque = 4

while True:
    Opcao = input(Menu)

    if Opcao == "1":
        valor = float(input('Informe o valor do deposito: '))
        if valor > 0:
            Saldo += valor
            Extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print('Operação Falhou! O valor valor informado é invalido')
    
    elif Opcao == "2":
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > Saldo
        excedeu_limite = valor > Limite
        excedeu_saques = Numero_de_Saque > Limite_de_Saque
        if excedeu_saldo:
            print("Operação Falhou, Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou, O valor do saldo excede o limite.")
        elif excedeu_saques:
            print("Operação Falhou, Numero de saques excedido.")
        elif valor > 0:
            Saldo -= valor
            Extrato += f'Saque: R${valor:.2f}\n'
            Numero_de_Saque += 1           
        else:
            print("Operação falhou, o valor informado é invalido.")
    
    elif Opcao == "3":
        print("\n================== EXTRATO ==================")
        print(" Não Foram realizadas movimentações:" if not Extrato else Extrato)
        print("=============================================")
        print(f'\nSaldo: R$ {Saldo:.2f}')
        print("=============================================")
    
    elif Opcao == "4":
        break
    
    else:
        print("Operação inválida: Por favor, selecione a opção desejada.")
    
