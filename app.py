# Declaracao inicial das variaveis de status da conta e acoes bancarias
saldo = round(0.00, 2);
valor_saque = round(0.00, 2);
valor_deposito = round(0.00, 2);

# Interface simples do banco

print('+-----------------------------------------------+')
print('+                BANCO SANTANDER                +')
print('+-----------------------------------------------+')
print('+ A sua conta bancaria foi criado com sucesso ! +')
print('+-----------------------------------------------+')
print('+ Faca o seu primeiro depósito para já comecar  +')
print('+ aproveitar a sua conta !!!                    +')
print('+-----------------------------------------------+')
print('+         Seu saldo atual é de : R${:.2f}         +'.format(saldo))

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
        match opcao:
            case "1":
                print("Pare!")
            case "2":
                print("Atenção!")
            case "3":
                print("Siga em frente")
            case "4":
                print("Siga em frente")
            case _:
                print("Cor desconhecida")
                exit()

    # Dando opcao de entrada da escolha para o usuario
    print('+     -----      OPCAO DESEJADA :      -----    +')
    print('+-----------------------------------------------+')
    # Recebendo a opcao
    escolha = input('+ Digite o número correspondente : ') 

    # Cahmando a funcao para continuar o switch case
    opcao_escolhida(escolha)




