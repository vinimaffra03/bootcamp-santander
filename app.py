# Declaracao inicial das variaveis de status da conta e acoes bancarias
saldo = float(0);
valor_saque = round(0.00, 2);

# exibir saldo
def exibe_saldo():
    print('+         Seu saldo atual é de : R${:.2f}        +'.format(saldo))  

# Interface simples do banco

print('+-----------------------------------------------+')
print('+                BANCO SANTANDER                +')
print('+-----------------------------------------------+')
print('+ A sua conta bancaria foi criado com sucesso ! +')
print('+-----------------------------------------------+')
print('+ Faca o seu primeiro depósito para já comecar  +')
print('+ aproveitar a sua conta !!!                    +')
print('+-----------------------------------------------+')
exibe_saldo()

# Este while vai ser usado pra rodar ate que seja digitado 5 ( sair )
while True:
    print('+-----------------------------------------------+')
    print('+         O que deseja fazer agora?             +')
    print('+-----------------------------------------------+')
    print('+         1 - CONSULTAR SALDO ATUAL :           +')
    print('+-----------------------------------------------+')
    print('+         2 - FAZER DEPÓSITO VIA TED :          +')
    print('+-----------------------------------------------+')
    print('+         3 - FAZER DEPÓSITO VIA PIX :          +')
    print('+-----------------------------------------------+')
    print('+         4 - REALIZAR SAQUE :                  +')
    print('+-----------------------------------------------+')
    print('+         5 - APENAS SAIR :                     +')
    print('+-----------------------------------------------+')

    # Decidindo qual acao realizar no banco
    def opcao_escolhida(opcao):
        global saldo  # Permite alterar o valor de saldo globalmente

        match opcao:
            # consultando saldo
            case "1":
                exibe_saldo()

            # deposito TED
            case "2":
                print('+-----------------------------------------------+')
                print('+               Depósito via TED                +')
                print('+-----------------------------------------------+')

                # solicitando valor de deposito ao usuario
                valor_deposito = float(input('+   Insira o valor no qual deseja depositar : '))

                # alterando valor atual do saldo/ atualizando
                saldo += valor_deposito

                print('+-----------------------------------------------+')
                print('+             AGUARDE UM INSTANTE...            +')
                print('+-----------------------------------------------+')
                print('+      Depósito de : R${:.2f} finalizado !      +'.format(valor_deposito))
                print('+-----------------------------------------------+')
                exibe_saldo()
                print('+-----------------------------------------------+')

            # deposito Pix
            case "3":
                print('+-----------------------------------------------+')
                print('+               Depósito via PIX                +')
                print('+-----------------------------------------------+')

                valor_deposito = float(input('+   Insira o valor no qual deseja depositar : '))
                saldo += valor_deposito

                print('+-----------------------------------------------+')
                print('+             AGUARDE UM INSTANTE...            +')
                print('+-----------------------------------------------+')
                print('+         PIX de : R${:.2f} finalizado !        +'.format(valor_deposito))
                print('+-----------------------------------------------+')
                exibe_saldo()
                print('+-----------------------------------------------+')

            # saldo disponivel
            case "4":
                print('+-----------------------------------------------+')
                print('+                 Realizar Saque                +')
                print('+-----------------------------------------------+')

                # solicitando valor de deposito ao usuario
                valor_saque = float(input('+   Insira o valor no qual deseja sacar : '))

                # alterando valor atual do saldo/ atualizando
                saldo -= valor_saque

                print('+-----------------------------------------------+')
                print('+             AGUARDE UM INSTANTE...            +')
                print('+-----------------------------------------------+')
                print('+        Saque de : R${:.2f} finalizado !       +'.format(valor_saque))
                print('+-----------------------------------------------+')
                exibe_saldo()
                print('+-----------------------------------------------+')

            # opcao para sair do menu
            case "5":
                print('+-----------------------------------------------+')
                print('        Agradecemos por usar nosso app! =D        ')
                print('+-----------------------------------------------+')
                exit()

            # opcao invalida
            case _:
                print('+-----------------------------------------------+')
                print('        Opção inválida. Tente novamente.         ')
                print('+-----------------------------------------------+')


    # Dando opcao de entrada da escolha para o usuario
    print('+     -----      OPCAO DESEJADA :      -----    +')
    print('+-----------------------------------------------+')
    # Recebendo a opcao
    escolha = input('+ Digite o número correspondente : ')
    print('+-----------------------------------------------+')

    # Cahmando a funcao para continuar o switch case
    opcao_escolhida(escolha)




