while True:
    print('menu de atividade')
    att = input('digite a atividade que voce quer ir de 1 a 8')


    if att == '1':
        nome =  input('digite o nome da pessoa')

        def mensagem(nome):
            print(f'{nome},Te desejo tudo de bom')

        men = mensagem(nome)

    # 2

    if att == '2':

        num1 = int(input('digite um numero inteiro: '))
        num2 = int(input('digite um numero inteiro: '))
        opcao = input('escolha a operação: ')

        while True:

            def soma(num1,num2):
                calculo = num1 + num2

            def subtracao(num1,num2):
                return num1 - num2

            def mutiplicacao(num1,num2):
                return num1 * num2

            def divisao(num1,num2):
                return num1 / num2

            resultado = soma()


    # 3 

    if att == '3':
        valores = []
        vetor = [ ]

        def resultado (vetor):
            vetor = valores
            del vetor[-1]
            return vetor


        while True:
            valor = input('digite um valor: ')
            valores.append(valor)
            if valor == 'pronto':
                break

        resposta = resultado(vetor)

        print(resposta)

    #4

    if att == '4':
        
        pares = []
        impares = []

        def eh_par(n):
            return n % 2 == 0

        while True:
            print('digite um numero inteiro')
            num = int(input())

            if eh_par(num):
                pares.append(num)
            else:
                impares.append(num)

            print('numeros par:')
            for p in pares:
                print(p)

            print('numeros impar:')
            for i in impares:
                print(i)



# 5 
    if att == '5':

        largura = float(input('digite a largura em metros do terreno: '))
        comprimento = float(input('digite o comprimento em metros do terreno: '))

        def area(largura,comprimento):
            area = largura * comprimento
            return area

        a = area(largura,comprimento)

        print(f'a área do terreno é:',a,'m²')



# 6
    if att ==  '6':
        taxaImposto = float(input('qual a taxa de imposto? '))
        custo = float(input('qual o custo do produto? ' ))

        def somaImposto(taxaImposto, custo):
            calculo = (taxaImposto/100) * custo
            return custo + calculo

        print(f'o valor final do produto com o imposto adicionado é:',somaImposto(taxaImposto, custo))


# 7
    if att == '7':
        tamanho = int(input('quantos elementos tera a lista? '))

        lista = []
        for i in range(tamanho):
            elemento = int(input(f'digite o elemento {i + 1}: '))
            lista.append(elemento)


        def elementos_repetidos(lista):
            repetidos = []
            for i in range(len(lista)):
                for j in range(i + 1, len(lista)):
                    if lista[i] == lista[j]:
                        if lista[i] not in repetidos:
                            repetidos.append(lista[i])
                        break
            return repetidos


        saida = elementos_repetidos(lista)
        print('Elementos que se repetem:', saida) 

#8 

    if att == '8':
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