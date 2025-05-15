
while True:
    print('operações disponíveis:')
    print('1 - depósito')
    print('2 - saque')
    print('3 - sair')

    escolha = input('escolha a operação 1, 2 ou 3: ')

    saldo = 0.0

    def deposito(saldo, valor):
        return saldo + valor

    def saque(saldo, valor):
        if valor > saldo:
            print('saque não permitido, saldo insuficiente.')
            return saldo
        
        else:
            return saldo - valor


    if escolha == '1':
        valor = float(input('digite o valor que voce quer depósitar: '))
        saldo = deposito(saldo, valor)
        print(f'depósito realizado, seu saldo atual é: R$ {saldo:.2f}')

    elif escolha == '2':
        valor = float(input('digite o valor que voce quer sacar: '))
        saldo = saque(saldo, valor)
        print(f'seu saldo atual é: R$ {saldo:.2f}')

    elif escolha == '3':
        break

    else:
        print('opção invalida, tente novamente')


print(f'operações finalizadas, seu saldo final na conta é : R$ {saldo:.2f}')